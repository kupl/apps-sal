L = sorted(list(map(int, input().split())), reverse=True)
ans = 0
if (L[1] - L[2]) % 2 != 0:
    L[0] += 1
    L[1] += 1
    ans += 1
ans += L[0] - L[1] + (L[1] - L[2]) // 2
print(ans)
