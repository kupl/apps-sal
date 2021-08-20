import sys
readline = sys.stdin.readline
read = sys.stdin.read
n = int(readline())
(*a,) = map(int, readline().split())
for i in range(n):
    a[i] -= i + 1
a.sort()
b = a[n // 2]
ans = sum((abs(ai - b) for ai in a))
print(ans)
