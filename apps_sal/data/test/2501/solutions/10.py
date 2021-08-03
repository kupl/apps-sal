from sys import stdin, stdout
# n,e=list(map(int,stdin.readline().split()))
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
d = {}
ans = 0
for i in range(n):
    d[a[i] + i] = d.get(a[i] + i, 0) + 1
for i in range(n):
    ans += d.get(i - a[i], 0)
print(ans)
