x, y, z = map(int, input().split())
sum = y + z + z
if x < sum:
    print(0)
else:
    ans = 1
    while sum <= x:
        sum += y + z
        ans += 1


    print(ans - 1)
