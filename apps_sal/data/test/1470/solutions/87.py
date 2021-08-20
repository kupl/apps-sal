N = int(input())
m = N % 11
ans = -(-N // 11) * 2
if 1 <= m <= 6:
    print(ans - 1)
else:
    print(ans)
