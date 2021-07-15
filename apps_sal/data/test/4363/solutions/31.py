K,S = map(int,input().split())
ans = 0
for i in range(K+1):
    for j in range(K+1):
        x = S - i - j
        if 0 <= x and x <= K:
            ans += 1
print(ans)
