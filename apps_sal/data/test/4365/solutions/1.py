k = int(input())
if k % 2 == 0:
    ans = k // 2 * (k // 2)
else:
    ans = (k - 1) // 2 * ((k + 1) // 2)
print(ans)
