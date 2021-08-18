from operator import itemgetter
n = int(input())
ai = [0] * n
bi = list(map(int, input().split()))
ai[-1] = bi[0]
for i in range(1, n // 2):
    mina = ai[i - 1]
    prev_end = ai[-i]
    num = max(mina, bi[i] - prev_end)
    ai[i] = num
    ai[-i - 1] = bi[i] - num
for i in range(n):
    print(ai[i], end=" ")
