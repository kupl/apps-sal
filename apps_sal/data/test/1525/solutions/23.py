H,W,K = list(map(int,input().split()))

goal = [0 for i in range(W)]
goal[0] = 1
oldGoal = [0 for i in range(W)]
oldGoal[0] = 1
fib = [1, 1, 2, 3, 5, 8, 13, 21, 34]

if W == 1:
    print(1)
    return

for i in range(H):
    for j in range(W):
        if j == 0:
            a1 = oldGoal[j] * fib[W-1]
            a2 = oldGoal[j+1] * fib[W-2]
            a1 = a1 % 1000000007
            a2 = a2 % 1000000007
            goal[j] = a1 + a2
        elif j == W - 1:
            a1 = oldGoal[j-1] * fib[W-2]
            a2 = oldGoal[j] * fib[W-1]
            a1 = a1 % 1000000007
            a2 = a2 % 1000000007
            goal[j] = a1 + a2
        else:
            a1 = oldGoal[j-1] * fib[j-1] * fib[W-j-1]
            a2 = oldGoal[j] * fib[j] * fib[W-j-1]
            a3 = oldGoal[j+1] * fib[j] * fib[W-j-2]
            a1 = a1 % 1000000007
            a2 = a2 % 1000000007
            a3 = a3 % 1000000007
            goal[j] = a1 + a2 + a3
    for k in range(W):
        oldGoal[k] = goal[k]
print(goal[K-1] % 1000000007)
