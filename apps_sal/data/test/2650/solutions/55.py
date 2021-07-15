from heapq import heappop, heappush

MAX = 2*10**5
n, q = list(map(int, input().split()))
ab = []
k_in = [[] for _ in range(MAX)]
k_out = [[] for _ in range(MAX)]
for i in range(n):
    a, b = list(map(int, input().split()))
    b -= 1
    ab.append([a, b])
    heappush(k_in[b], -a)

k_max_in = []
k_max_out = []
for i in range(MAX):
    if k := k_in[i]:
        heappush(k_max_in, -k[0])

for _ in range(q):
    c, d = [int(x)-1 for x in input().split()]
    idx = ab[c][1]
    heappush(k_max_out, -k_in[idx][0])
    if k_in[d]:
        heappush(k_max_out, -k_in[d][0])
    while k_max_out and k_max_in[0] == k_max_out[0]:
        heappop(k_max_in)
        heappop(k_max_out)
    heappush(k_out[idx], -ab[c][0])
    while k_out[idx] and k_in[idx][0] == k_out[idx][0]:
        heappop(k_in[idx])
        heappop(k_out[idx])

    heappush(k_in[d], -ab[c][0])
    if k_in[idx]:
        heappush(k_max_in, -k_in[idx][0])
    heappush(k_max_in, -k_in[d][0])
    ab[c][1] = d

    print((k_max_in[0]))

