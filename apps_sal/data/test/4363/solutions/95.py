def LI():
    return list(map(int, input().split()))


K, S = LI()
ans = 0
for i in range(K+1):
    for j in range(K+1):
        if 0 <= S-(i+j) <= K:
            ans += 1
print(ans)

