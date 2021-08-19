import heapq
n = input()
A = list(map(int, input().split()))
if len(A) % 2 == 0:
    A.append(0)
st = 0
heapq.heapify(A)
while len(A) > 1:
    abc = 0
    a = heapq.heappop(A)
    b = heapq.heappop(A)
    c = heapq.heappop(A)
    abc = a + b + c
    st = st + abc
    heapq.heappush(A, abc)
print(st)
