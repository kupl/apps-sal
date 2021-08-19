x = int(input())
ans = x // 11 * 2
amari = x % 11
if amari == 0:
    print(ans)
elif amari <= 6:
    print(ans + 1)
else:
    print(ans + 2)
