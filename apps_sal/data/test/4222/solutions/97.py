(N, K) = map(int, input().split())
sunuke = [0] * N
for _ in range(K):
    d = int(input())
    temp = list(map(int, input().split()))
    for j in temp:
        sunuke[j - 1] += 1
ans = 0
for k in range(len(sunuke)):
    if sunuke[k] == 0:
        ans += 1
print(ans)
