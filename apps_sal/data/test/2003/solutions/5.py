trie = [[-1, -1]]
counts = [0]
trie_size = 1


def insert(x):
    nonlocal trie, counts, trie_size

    node = 0
    out = []
    for i in range(30, -1, -1):
        b = 0 if (x & (1 << i)) == 0 else 1
        out.append(str(b))
        if trie[node][b] == -1:
            trie[node][b] = trie_size
            trie.append([-1, -1])
            counts.append(0)
            trie_size += 1

        counts[node] += 1
        node = trie[node][b]

    counts[node] += 1
    # print('+', ''.join(out))


def remove(x):
    nonlocal trie, counts, trie_size
    node = 0
    for i in range(30, -1, -1):
        counts[node] -= 1

        b = 0 if (x & (1 << i)) == 0 else 1
        node = trie[node][b]

    counts[node] -= 1


def query(x):
    nonlocal trie, counts, trie_size
    node = 0
    ans = 0

    out = []
    path = []
    for i in range(30, -1, -1):
        b = 0 if (x & (1 << i)) == 0 else 1
        out.append(str(b))

        if trie[node][1 - b] == -1 or counts[trie[node][1 - b]] == 0:
            node = trie[node][b]
            ans |= (1 << i) * b
            path.append(str(b))
        else:
            node = trie[node][1 - b]
            ans |= (1 << i) * (1 - b)
            path.append(str(1 - b))

    # print(''.join(out))
    # print('path', ''.join(path))
    return ans ^ x


def main():
    q = int(input())
    insert(0)
    for _ in range(q):
        # print(trie)
        # print(counts)

        a, b = input().split()
        b = int(b)
        if a == '+':
            insert(b)
        elif a == '-':
            remove(b)
        else:
            print(query(b))


main()
