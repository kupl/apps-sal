n = int(input())
an = list(sorted(map(int, input().split())))

ans = sum(an)-n
for i in range(2, 10**5):
    newa = 0
    for j in range(n):
        newa += abs(an[j]-i**j)
        if newa >= ans:
            break
    if newa < ans:
        ans = newa

print(ans)

