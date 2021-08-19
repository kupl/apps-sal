N = int(input())
ans = 0
CN = 0
while CN < N:
    ans += 1
    CN += ans
print(ans)
