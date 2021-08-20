import heapq
n = int(input())
resp = 0
test = [int(i) for i in input().split()]
test.sort()
if n % 2 == 0:
    test = [0] + test
    n += 1
while n != 1:
    c = heapq.heappop(test) + heapq.heappop(test) + heapq.heappop(test)
    resp += c
    heapq.heappush(test, c)
    n -= 2
print(resp)
