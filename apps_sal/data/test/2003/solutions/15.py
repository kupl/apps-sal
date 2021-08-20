class Node:

    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, x):
        self.temp = self.root
        for i in range(31, -1, -1):
            curbit = x >> i & 1
            if curbit:
                if not self.temp.right:
                    self.temp.right = Node()
                self.temp = self.temp.right
                self.temp.cnt += 1
            else:
                if not self.temp.left:
                    self.temp.left = Node()
                self.temp = self.temp.left
                self.temp.cnt += 1

    def remove(self, x):
        self.temp = self.root
        for i in range(31, -1, -1):
            curbit = x >> i & 1
            if curbit:
                self.temp = self.temp.right
                self.temp.cnt -= 1
            else:
                self.temp = self.temp.left
                self.temp.cnt -= 1

    def maxxor(self, x):
        self.temp = self.root
        self.ss = 0
        for i in range(31, -1, -1):
            curbit = x >> i & 1
            if curbit:
                if self.temp.left and self.temp.left.cnt:
                    self.ss += 1 << i
                    self.temp = self.temp.left
                elif self.temp.right:
                    self.temp = self.temp.right
            elif self.temp.right and self.temp.right.cnt:
                self.ss += 1 << i
                self.temp = self.temp.right
            elif self.temp.left:
                self.temp = self.temp.left
        return self.ss


q = int(input())
trie = Trie()
trie.insert(0)
for _ in range(0, q):
    qq = input().split()
    if qq[0] == '+':
        trie.insert(int(qq[1]))
    elif qq[0] == '-':
        trie.remove(int(qq[1]))
    else:
        print(trie.maxxor(int(qq[1])))
'\n\n10\n+ 8\n+ 9\n+ 11\n+ 6\n+ 1\n? 3\n- 8\n? 3\n? 8\n? 11\n\n\n10\n? 1\n+ 1\n+ 8\n- 1\n+ 2\n+ 7\n+ 4\n+ 7\n+ 3\n? 7\n\n\n\n\n'
