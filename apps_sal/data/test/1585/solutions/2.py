x, y = list(map(int, input().split()))
ans = len(str(bin(y // x))) -2
print(ans)

