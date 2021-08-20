import heapq
N = int(input())
A = [int(a) for a in input().split()]
L = A[:2 * N]
L.sort()
s1 = 0
s2 = 0
h1 = []
h2 = []
dic = {}
dic_h = {}
for i in range(N):
    heapq.heappush(h1, -L[i])
    if L[i] in dic_h:
        dic_h[L[i]] += 1
    else:
        dic_h[L[i]] = 1
    s1 += L[i + N]
    if L[i + N] in dic:
        dic[L[i + N]] += 1
    else:
        dic[L[i + N]] = 1
    s2 += A[i + 2 * N]
    heapq.heappush(h2, -A[i + 2 * N])
ans = s1 - s2
for i in range(2 * N - 1, N - 1, -1):
    if A[i] + h2[0] < 0:
        s2 += heapq.heappop(h2)
        heapq.heappush(h2, -A[i])
        s2 += A[i]
    if A[i] in dic:
        if dic[A[i]] > 0:
            dic[A[i]] -= 1
            s1 -= A[i]
            t = -heapq.heappop(h1)
            while h1:
                if dic_h[t] > 0:
                    dic_h[t] -= 1
                    break
                else:
                    t = -heapq.heappop(h1)
            s1 += t
            if t in dic:
                dic[t] += 1
            else:
                dic[t] = 1
    else:
        dic_h[A[i]] -= 1
    ans = max(ans, s1 - s2)
print(ans)
