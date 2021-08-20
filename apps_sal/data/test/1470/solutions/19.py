x = int(input())
ans = x // 11 * 2
q = x % 11
if q == 0:
    print(ans)
elif q <= 6:
    print(ans + 1)
else:
    print(ans + 2)
