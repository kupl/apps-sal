import heapq

def divisor(i):
    s = []
    for j in range(1, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            s.append(i // j)
            s.append(j)
    return sorted(set(s))

n, k = map(int, input().split())
a = list(map(int, input().split()))
suma = sum(a)
s = divisor(suma)
for i in range(1, len(s) + 1):
    x = s[-i]
    y = suma // x
    h = []
    heapq.heapify(h)
    for j in a:
        y -= j // x
        heapq.heappush(h, -(j % x))
    cnt = 0
    for _ in range(y):
        cnt += (heapq.heappop(h) % x)
    if cnt <= k:
        print(x)
        return
