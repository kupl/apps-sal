from heapq import heapify, heappush, heappop
n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
s = input()
h = [A[0]]
heapify(h)
ans = A[0]
for i in range(1, n):
    if s[i] == s[i - 1]:
        if len(h) == k:
            elem = heappop(h)
            if elem > A[i]:
                heappush(h, elem)
            else:
                heappush(h, A[i])
                ans += (A[i] - elem)
        else:
            heappush(h, A[i])
            ans += A[i]
    else:
        h = [A[i]]
        heapify(h)
        ans += A[i]
print(ans)
