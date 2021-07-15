AMAX = 10**5
count = [0] * (AMAX + 1)

N, K = map(int, input().split())

for _ in range(N):
    a, b = map(int, input().split())
    count[a] += b

for ans in range(AMAX + 1):
    if K <= count[ans]:
        print(ans)
        break
    K -= count[ans]
