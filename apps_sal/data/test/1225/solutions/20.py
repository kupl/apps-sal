H = int(input())
count = 1
ans = 0
while H > 0:
    H = int(H // 2)
    ans += count
    count *= 2
print(ans)
