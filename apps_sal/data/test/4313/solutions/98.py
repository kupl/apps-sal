n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

vc = []
for i, j in zip(v, c):
    vc.append(i-j)
vc = sorted(vc, reverse=True)
ans = 0
for i in vc:
    if i <= 0:
        break
    ans += i
print(ans)
