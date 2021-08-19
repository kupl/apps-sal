import heapq
(X, Y, Z, K) = list(map(int, input().split()))
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
h = []
heapq.heappush(h, (-A[0] - B[0] - C[0], 0, 0, 0))
ans = []
st = set()
for _ in range(K):
    (s, i, j, k) = heapq.heappop(h)
    ans.append(-s)
    if i + 1 < X and (not (i + 1, j, k) in st):
        heapq.heappush(h, (-A[i + 1] - B[j] - C[k], i + 1, j, k))
        st.add((i + 1, j, k))
    if j + 1 < Y and (not (i, j + 1, k) in st):
        heapq.heappush(h, (-A[i] - B[j + 1] - C[k], i, j + 1, k))
        st.add((i, j + 1, k))
    if k + 1 < Z and (not (i, j, k + 1) in st):
        heapq.heappush(h, (-A[i] - B[j] - C[k + 1], i, j, k + 1))
        st.add((i, j, k + 1))
for v in ans:
    print(v)
