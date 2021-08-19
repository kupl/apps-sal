import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = [i for i in range(1, n)]
p.append(0)
ans = []
count = [0] * n
for i in b:
    count[i] += 1
for i in a:
    v = (n - i) % n
    while count[v] == 0:
        if count[p[v]] == 0:
            p[v] = p[p[v]]
        v = p[v]
    count[v % n] -= 1
    ans.append((v + i) % n)
print(' '.join(map(str, ans)))
