(N, K) = map(int, input().split())
sunuke = [1] * N
for i in range(K):
    di = int(input())
    tmp = map(int, input().split())
    for j in tmp:
        sunuke[j - 1] = 0
print(sum(sunuke))
