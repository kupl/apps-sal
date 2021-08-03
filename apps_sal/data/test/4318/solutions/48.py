N = int(input())
H = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(0, i):
        if H[j] > H[i]:
            ans -= 1
            break
    ans += 1
print(ans)
