import heapq as h
n = int(input())
ai = [int(i) for i in input().split()]
if n % 2 == 0:
    ai = [0] + ai
result = 0
h.heapify(ai)
while len(ai) > 1:
	a1 = h.heappop(ai)
	a2 = h.heappop(ai)
	a3 = h.heappop(ai)
	result += a1 + a2 + a3
	h.heappush(ai, a1 + a2 + a3)
print(result)
