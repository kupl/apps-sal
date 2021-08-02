x, y, z = [int(i) for i in input().split()]
ans = x // (y + z)
if x - (ans * (y + z)) < z:
    ans -= 1
print(ans)
