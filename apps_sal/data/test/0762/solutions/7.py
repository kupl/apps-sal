(n, B) = list(map(int, input().split()))
a = list(map(int, input().split()))
oMe = 0
Bs = []
for i in range(n):
    if a[i] % 2 == 0:
        oMe -= 1
    else:
        oMe += 1
    if oMe == 0 and i + 1 != n:
        Bs.append(abs(a[i] - a[i + 1]))
Bs = sorted(Bs)
ans = 0
for i in range(len(Bs)):
    if B - Bs[i] >= 0:
        B -= Bs[i]
        ans += 1
print(ans)
