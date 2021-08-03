n = int(input())
s = sorted([int(input()) for _ in range(n)])
ans = sum(s)
for v in s:
    if ans % 10 != 0:
        print(ans)
        break
    if v % 10 != 0:
        ans -= v
else:
    print(0)
