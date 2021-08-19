n = int(input())
ai = list(map(int, input().split()))
bi = [0] * n
bi[n - 1] = ai[n - 1]
for i in range(n - 2, -1, -1):
    bi[i] = ai[i] + ai[i + 1]
for i in range(n):
    print(bi[i], end=' ')
