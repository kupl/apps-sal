from operator import itemgetter
# int(input())
# map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
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
