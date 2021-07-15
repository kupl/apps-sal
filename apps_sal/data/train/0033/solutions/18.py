t = int(input())
for _ in range(t):
    n = int(input())
    A = list(range(1, n+1))
    ans = []
    t = -1
    for i in range(n-1):
        ans.append((A[-2], A[-1]))
        x = A.pop()
        if (x+A[-1])%2 == 0:
            A[-1] = (x+A[-1])//2
        else:
            A[-1] = (x+A[-1]+1)//2
    print(A[0])
    for i in range(len(ans)):
        print(*ans[i])

