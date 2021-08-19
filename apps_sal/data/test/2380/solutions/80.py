import bisect
import sys
input = sys.stdin.readline
(n, m) = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
minA = A[0]
Query = []
for _ in range(m):
    (b, c) = map(int, input().split())
    if c > minA:
        Query.append([b, c])
Query = sorted(Query, key=lambda x: (x[1], x[0]), reverse=True)
ans = 0
index = 0
for (b, c) in Query:
    if index >= n:
        break
    cnt = 0
    Flag = True
    while Flag:
        if A[index] < c:
            A[index] = c
            cnt += 1
            index += 1
            if cnt >= b or index >= n:
                Flag = False
        else:
            Flag = False
    '\n    #A.sort()\n    if A[0] >= c:\n        break\n    else:\n        index = min(bisect.bisect_left(A,c),b)\n        if index > len(A):\n            ans += c * len(A)\n            break\n        else:\n            ans += c * index\n            A = A[index:]\n    print(A)\n    '
print(sum(A))
