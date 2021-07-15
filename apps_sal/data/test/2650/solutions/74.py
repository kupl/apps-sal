import heapq

N, Q = map(int, input().split())

M = 2 * 10**5

rate_list = []
rates = [[] for _ in range(M)]
members = [set() for _ in range(M)]
belongs = [-1] * N

for i in range(N):
    A, B = map(int, input().split())
    B = B - 1
    heapq.heappush(rates[B], (-A, i))
    members[B].add(i)
    belongs[i] = B
    rate_list.append(A)

max_rates = []
for num, rate in enumerate(rates):
    if len(rate) > 0:
        heapq.heappush(max_rates, (-rate[0][0], num))

for i in range(Q):
    C, D = map(int, input().split())
    C = C - 1
    D = D - 1
    old = belongs[C]
    belongs[C] = D
    members[old].remove(C)
    members[D].add(C)
    while len(rates[old]) > 0 and rates[old][0][1] not in members[old]:
        heapq.heappop(rates[old])
    
    if len(rates[old]) > 0:
        heapq.heappush(max_rates, (-rates[old][0][0], old))
        
    heapq.heappush(rates[D], (-rate_list[C], C))
    heapq.heappush(max_rates, (rate_list[C], D))

    while max_rates:
        rate, num = max_rates[0]
        if len(rates[num])==0 or - rates[num][0][0] != rate:
            heapq.heappop(max_rates)
        else:
            print(rate)
            break
