def f():
    n = int(input())
    A = [int(s) for s in input().split()]
    ans = [0] * n
    ans[0] = 1
    ans[n - 1] = 1
    i = 0
    j = n - 1
    outMin = n + 1
    while j > i:
        if A[i] > A[j]:
            if A[i] < outMin:
                outMin = A[i]
            i += 1
        else:
            if A[j] < outMin:
                outMin = A[j]
            j -= 1
        if j - i == outMin - 2:
            ans[j - i] = 1
    print(''.join(str(i) for i in ans))


t = int(input())
for i in range(t):
    f()
