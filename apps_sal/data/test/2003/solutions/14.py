import sys
input = sys.stdin.readline


class BinaryTrie:

    class Node:

        def __init__(self, bit: bool = False):
            self.bit = bit
            self.children = []
            self.count = 0
            self.counter = 1

    def __init__(self, size):
        self.root = BinaryTrie.Node()
        self.size = size

    def convert(self, key):
        """Converts key from string/integer to a list of boolean values!"""
        bits = []
        if isinstance(key, int):
            key = bin(key)[2:]
        if isinstance(key, str):
            for i in range(self.size - len(key)):
                bits += [False]
            for i in key:
                if i == '0':
                    bits += [False]
                else:
                    bits += [True]
        else:
            return list(key)
        return bits

    def add(self, key):
        """Add a key to the trie!"""
        node = self.root
        bits = self.convert(key)
        for bit in bits:
            found_in_child = False
            for child in node.children:
                if child.bit == bit:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = BinaryTrie.Node(bit)
                node.children.append(new_node)
                node = new_node
        node.count += 1

    def remove(self, key):
        """Removes a key from the trie! If there are multiple occurences, it removes only one of them."""
        node = self.root
        bits = self.convert(key)
        nodelist = [node]
        for bit in bits:
            for child in node.children:
                if child.bit == bit:
                    node = child
                    node.counter -= 1
                    nodelist.append(node)
                    break
        node.count -= 1
        if not node.children and (not node.count):
            for i in range(len(nodelist) - 2, -1, -1):
                nodelist[i].children.remove(nodelist[i + 1])
                if nodelist[i].children or nodelist[i].count:
                    break

    def query(self, prefix, root=None):
        """Search for a prefix in the trie! Returns the node if found, otherwise 0."""
        if not root:
            root = self.root
        node = root
        if not root.children:
            return 0
        for bit in prefix:
            bit_not_found = True
            for child in node.children:
                if child.bit == bit:
                    bit_not_found = False
                    node = child
                    break
            if bit_not_found:
                return 0
        return node


di = {}
tr = BinaryTrie(32)
tr.add(0)
for _ in range(int(input())):
    (a, b) = input().split()
    if a == '+':
        tr.add(int(b))
    elif a == '-':
        tr.remove(int(b))
    else:
        ans = 0
        node = tr.root
        cnt = 32
        y = bin(int(b))[2:]
        x = [False if i == '0' else True for i in '0' * (32 - len(y)) + y]
        for i in x:
            cnt -= 1
            next = tr.query([not i], node)
            if not next:
                node = tr.query([i], node)
            else:
                node = next
                ans += 2 ** cnt
        print(ans)
