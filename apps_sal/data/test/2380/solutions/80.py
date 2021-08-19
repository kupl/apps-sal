import bisect
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

minA = A[0]
Query = []
for _ in range(m):
    b, c = map(int, input().split())
    if c > minA:
        Query.append([b, c])
Query = sorted(Query, key=lambda x: (x[1], x[0]), reverse=True)

ans = 0
index = 0
for b, c in Query:
    if index >= n:
        break
    # print("----")
    cnt = 0
    Flag = True
    while Flag:
        # print(A,b,c,index)
        if A[index] < c:
            A[index] = c
            cnt += 1
            index += 1
            if (cnt >= b) or (index >= n):
                Flag = False
        else:
            Flag = False
    '''
    #A.sort()
    if A[0] >= c:
        break
    else:
        index = min(bisect.bisect_left(A,c),b)
        if index > len(A):
            ans += c * len(A)
            break
        else:
            ans += c * index
            A = A[index:]
    print(A)
    '''
print(sum(A))
