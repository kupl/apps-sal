int_size = 32


class TrieNode:
    def __init__(self):
        self.child = [None] * 2
        self.value = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        curr = self.root

        for i in range(int_size - 1, -1, -1):
            current_bit = 1 if (key & (1 << i)) else 0

            if curr.child[current_bit] == None:
                curr.child[current_bit] = TrieNode()

            curr = curr.child[current_bit]

        curr.value = key

    def max_xor(self, key):
        curr = self.root
        for i in range(int_size - 1, -1, -1):
            current_bit = 1 if (key & (1 << i)) else 0

            if curr.child[1 - current_bit] != None:
                curr = curr.child[1 - current_bit]
            elif curr.child[current_bit] != None:
                curr = curr.child[current_bit]
            else:
                raise Exception("Something is not right!!")

        return key ^ curr.value


n = int(input())
arr = list(map(int, input().split()))
tree = Trie()
tree.insert(0)

ans = 0
now = 0
for i in range(n):
    now = now ^ arr[i]
    tree.insert(now)
    ans = max(ans, tree.max_xor(now))

print(ans)
