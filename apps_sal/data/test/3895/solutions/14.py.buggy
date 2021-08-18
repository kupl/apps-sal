import sys

n = int(input())
s = input().split()
a = [int(i) for i in s]
a.insert(0, 0)

hash = [0 for i in range(n + 1)]
g = [0 for i in range(n + 1)]
h = [0 for i in range(n + 1)]
index = 1

for i in range(1, n + 1):
    if hash[a[i]] == 0:
        if index > n:
            print(-1)
            return
        hash[a[i]] = index
        g[i] = index
        h[index] = a[i]
        index += 1
    else:
        g[i] = hash[a[i]]

for i in range(1, index):
    if g[h[i]] != i:
        print(-1)
        return

print(index - 1)
print(' '.join([str(i) for i in g[1:n + 1]]))
print(' '.join([str(i) for i in h[1:index]]))
