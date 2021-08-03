X, Y, Z = map(int, input().split())
L = X - Z
ans = 0
for i in range(1000000):
    if L >= (Z + Y) * i:
        ans = i
    else:
        break
print(ans)
