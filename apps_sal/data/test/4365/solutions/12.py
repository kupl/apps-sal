k = int(input())

if k % 2 == 0:
    ans = (k // 2)**2
else:
    ans = (k // 2) * (k // 2 + 1)

print(ans)
