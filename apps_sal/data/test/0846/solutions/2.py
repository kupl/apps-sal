(n, m) = map(int, input().split())
L = list(map(int, input().split()))
Q = [1] * n
Ans = [-1] * n
for i in range(m):
    x = L[i] - 1
    for j in range(x, n):
        if Q[j] == 1:
            Q[j] = 0
            Ans[j] = x + 1
for item in Ans:
    print(item, end=' ')
