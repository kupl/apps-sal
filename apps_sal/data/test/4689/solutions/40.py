try:
    K, N = map(int,input().split())
    A = list(map(int, input().split()))

    li = []
    for i in range(N - 1):
        li.append(A[i + 1] - A[i]) 

    li.append(abs(A[0] + (K - A[-1])))
    print(sum(li) - max(li))
except:
    pass
