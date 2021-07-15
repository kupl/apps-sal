class Node:
    def __init__(self, key=None):
        self.key = key
        self.balance = 'E'
        self.parent = None
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = Node()
        self.root.parent = Node('nil')

    def insert(self, key):
        if self.root.key is None:
            self.root.key = key
            return
        cursor = self.root
        while cursor:
            p = cursor
            if key == cursor.key:
                return
            elif key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        new_node = Node(key)
        new_node.parent = p
        if key < p.key:
            p.left = new_node
        else:
            p.right = new_node
            
        return self.rebalance(p, new_node, key)
            
    def rebalance(self, u, v, key):
        while u.key != 'nil':
            if u.key > v.key:
                if u.balance == 'R':
                    u.balance = 'E'
                    return
                elif u.balance == 'L':
                    if v.balance == 'L':
                        self.rotate_R(u, v)
                        return
                    elif v.balance == 'R':

                        self.rotate_LR(u, v)
                        return
                else:
                    u.balance = 'L'
                    v = u
                    u = u.parent
            else:
                if u.balance == 'L':
                    u.balance = 'E'
                    return
                elif u.balance == 'R':
                    if v.balance == 'R':
                        self.rotate_L(u, v)
                        return
                    elif v.balance == 'L':
                        self.rotate_RL(u, v)
                        return
                else:
                    u.balance = 'R'
                    v = u
                    u = u.parent
              
    def replace(self, u, v):
        if u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
        if v.parent.key == 'nil':
            self.root = v   

    def rotate_R(self, u, v):
        w = v.right

        self.replace(u, v)
        v.right = u
        u.parent = v        
        u.left = w        
        if w:
            w.parent = u
        u.balance = 'E'
        v.balance = 'E'           

    def rotate_L(self, u, v):
        w = v.left
        
        self.replace(u, v)
        v.left = u
        u.parent = v
        u.right = w        
        if w:
            w.parent = u
        u.balance = 'E'
        v.balance = 'E' 

    def rotate_LR(self, u, v):
        w = v.right
        
        self.replace(u, w)
        if w.left:
            v.right = w.left
            v.right.parent = v
        else:
            v.right = None
        if w.right:
            u.left = w.right
            u.left.parent = u
        else:
            u.left = None
        v.parent = w
        w.left = v
        u.parent = w
        w.right = u

        if w.balance == 'R':
            u.balance = 'E'
            v.balance = 'L'
        elif w.balance == 'L':
            u.balance ='R'
            v.balance = 'E'
        else:
            u.balance = 'E'
            v.balance = 'E'
        w.balance = 'E'        

    def rotate_RL(self, u, v):
        w = v.left
        
        self.replace(u, w)
        if w.left:
            w.left.parent = u
            u.right = w.left
        else:
            u.right = None
        if w.right:
            w.right.parent = v
            v.left = w.right
        else:
            v.left = None
        u.parent = w
        w.left = u
        v.parent = w
        w.right = v       
        
        if w.balance == 'R':
            u.balance = 'L'
            v.balance = 'E'
        elif w.balance == 'L':
            u.balance ='E'
            v.balance = 'R'
        else:
            u.balance = 'E'
            v.balance = 'E'
        w.balance = 'E'

    def find(self, key):
        cursor = self.root
        while cursor:
            if cursor.key == key:
                return cursor
            if key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        return None
    
    def next_greater_key(self, cursor):
        if cursor is None:
            return
        if cursor.right:
            cursor = cursor.right
            while cursor.left:
                cursor = cursor.left
            return cursor
        elif cursor.parent.left == cursor:
            return cursor.parent
        elif cursor.parent.right == cursor:
            while cursor.parent.key != 'nil' and cursor.parent.right == cursor:
                cursor = cursor.parent
            if cursor.parent.key != 'nil':
                return cursor.parent
        else:
            return None
        
    def next_smaller_key(self, cursor):
        if cursor is None:
            return 
        if cursor.left:
            cursor = cursor.left
            while cursor.right:
                cursor = cursor.right
            return cursor
        elif cursor.parent.right == cursor:
            return cursor.parent
        elif cursor.parent.left == cursor:
            while cursor.parent.key != 'nil' and cursor.parent.left == cursor:
                cursor = cursor.parent
            if cursor.parent.key != 'nil':
                return cursor.parent
        
    def get_smaller_key(self, key):
        cursor = self.find(key)
        l1 = self.next_smaller_key(cursor)
        l2 = self.next_smaller_key(l1)
        if l2 is None:
            l2 = 0
        else:
            l2 = l2.key
        return l1.key, l2
    
    def get_greater_key(self, key):
        cursor = self.find(key)
        r1 = self.next_greater_key(cursor)
        r2 = self.next_greater_key(r1)
        if r2 is None:
            r2 = 0
        else:
            r2 = r2.key
        return r1.key, r2


def main():
#    import random
    import sys

#    N = 100000
#    P = list(range(1, N + 1))
#    random.shuffle(P)
    
    input = sys.stdin.readline
    N = int(input())
    P = map(int, input().split())    
    
    idx = [-1] * (N + 1)
    for i, v in enumerate(P, 1):
        idx[v] = i
    avl = AVL()
    for i in [0, idx[N], N+1]:
        avl.insert(i)
    total = 0
    for j in range(N - 1, 0, -1):
        n = idx[j]
        avl.insert(n)
        
        l1_idx , l2_idx = avl.get_smaller_key(n)
        l1 = n - l1_idx
        if l1_idx != 0:
            l2 = l1_idx - l2_idx
        else:
            l2 = 0
            
        r1_idx, r2_idx = avl.get_greater_key(n)
        r1 = r1_idx - n
        if r1_idx != N + 1:
            r2 = r2_idx - r1_idx
        else:
            r2 = 0
            
        cnt = (l1 * r2 + r1 * l2) * j
        total += cnt
    
    print(total)
    
def __starting_point():
    main()
__starting_point()
