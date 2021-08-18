import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
w = [int(i) for i in input().split()]
arr = [(int(i) - 1) for i in input().split()]
v = []
s = 0
used = [False] * n
for i in range(m):
    if not used[arr[i]]:
        used[arr[i]] = True
        v.append(arr[i])
for i in range(m):
    j = 0
    while v[j] != arr[i]:
        s += w[v[j]]
        j += 1
    v = [v[j]] + v[0:j] + v[j + 1:]
print(s)
