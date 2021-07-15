rs = lambda : int(input())
ri = lambda : list(map(int, input().split()))
rli = lambda : list(map(int, input().split()))

n = int(input())
a = rli()

mx = 0
ans = 0
for i in range(n):
    mx = max(mx, a[i]-1)
    if mx == i:
        ans += 1

print(ans)

