n, m, ta, tb, k = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if k >= min(n, m):
    print(-1)
else:
    result = -1
    for i in range(k + 1):
        num = A[i] + ta
        #print(i, num)
        left = -1
        right = m
        while left + 1 != right:
            mid = (left + right) // 2
            if B[mid] >= num:
                right = mid
            else:
                left = mid
        end = right + k - i
        if end < m:
            result = max(result, B[end] + tb)
        else:
            print(-1)
            break
    else:
        print(result)
            

