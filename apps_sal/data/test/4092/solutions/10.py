import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
done = {a[0]: 0, 0: 0}
s = a[0]
ans = 0
for i in range(1, n):
    s += a[i]
    if s in done:
        done = {0: 0, a[i]: 0}
        ans += 1
        s = a[i]
    else:
        done[s] = 0
print(ans)
