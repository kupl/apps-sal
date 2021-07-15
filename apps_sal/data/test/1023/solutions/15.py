n,m,ta,tb,k = list(map(int,input().split()))

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

res = -1
j = 0
if k < len(A):
    for i in range(k+1):
        if i < len(A):
            t = A[i] + ta
            while j < len(B) and B[j] < t:
                j += 1
            togo = k - i
            jj = j + togo
            if jj < len(B):
                res = max(res, B[jj] + tb)
            else:
                res = -1
                break
print(res)



