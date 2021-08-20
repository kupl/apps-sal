def num_to_bitstring(n):
    """converts num to bitstring of length 30"""
    b = bin(n)
    assert b[:2] == '0b'
    b = b[2:]
    return '0' * (30 - len(b)) + b


class Node:

    def __init__(self, val=0):
        self.value = val
        self.left = None
        self.right = None

    def add(self):
        self.value = self.value + 1


class Trie:

    def __init__(self):
        self.head = Node(1)

    def add(self, s):
        current = self.head
        for b in s:
            if b == '0':
                if current.left == None:
                    current.left = Node()
                    current = current.left
                else:
                    current = current.left
            elif b == '1':
                if current.right == None:
                    current.right = Node()
                    current = current.right
                else:
                    current = current.right
        current.value = current.value + 1

    def subtract(self, s):
        current = self.head
        last_branch = None
        for b in s:
            if current.left != None and current.right != None:
                if b == '0':
                    last_branch = (current, '0')
                elif b == '1':
                    last_branch = (current, '1')
            if b == '0':
                current = current.left
            elif b == '1':
                current = current.right
        current.value = current.value - 1
        if current.value == 0:
            if last_branch[1] == '0':
                last_branch[0].left = None
            elif last_branch[1] == '1':
                last_branch[0].right = None

    def xor(self, s):
        sum = 0
        i = 29
        current = self.head
        for b in s:
            if b == '0':
                if current.right != None:
                    current = current.right
                    sum += 2 ** i
                else:
                    current = current.left
            elif current.left != None:
                current = current.left
                sum += 2 ** i
            else:
                current = current.right
            i -= 1
        return sum


def main():
    t = Trie()
    s = num_to_bitstring(0)
    t.add(s)
    q = int(input())
    for a0 in range(q):
        query = input()
        s = num_to_bitstring(int(query[2:]))
        if query[0] == '+':
            t.add(s)
        elif query[0] == '-':
            t.subtract(s)
        elif query[0] == '?':
            print(t.xor(s))


main()
