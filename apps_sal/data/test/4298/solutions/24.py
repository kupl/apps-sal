a, b = list(map(int, input().split()))
ans = a // (b * 2 + 1)
if ans == a / (b * 2 + 1):
    print(ans)
else:
    print((ans + 1))
