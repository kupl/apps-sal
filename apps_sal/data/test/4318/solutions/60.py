N = int(input())
H = list(map(int, input().split()))
highest = H[0]
ans = 0

for i in range(N):
    if highest <= H[i]:
        highest = H[i]
        ans += 1

print(ans)
