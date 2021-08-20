__author__ = 'Rajan'
(n, m) = map(int, input().split())
hash = [False for i in range(n + 1)]
for i in range(m):
    (a, b) = map(int, input().split())
    hash[a] = hash[b] = True
b = 0
for i in range(1, n + 1):
    if not hash[i]:
        b = i
        break
print(n - 1)
for i in range(1, n + 1):
    if i != b:
        print(i, b)
