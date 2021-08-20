import heapq
(X, Y, Z, K) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
dic = {}
dic[0, 0, 0] = 1
lst = [(-(A[0] + B[0] + C[0]), 0, 0, 0)]
heapq.heapify(lst)
for r in range(K):
    a = lst[0][1]
    b = lst[0][2]
    c = lst[0][3]
    print(lst[0][0] * -1)
    heapq.heappop(lst)
    if a < X - 1:
        if (a + 1, b, c) not in dic:
            heapq.heappush(lst, (-(A[a + 1] + B[b] + C[c]), a + 1, b, c))
            dic[a + 1, b, c] = 1
    if b < Y - 1:
        if (a, b + 1, c) not in dic:
            heapq.heappush(lst, (-(A[a] + B[b + 1] + C[c]), a, b + 1, c))
            dic[a, b + 1, c] = 1
    if c < Z - 1:
        if (a, b, c + 1) not in dic:
            heapq.heappush(lst, (-(A[a] + B[b] + C[c + 1]), a, b, c + 1))
            dic[a, b, c + 1] = 1
