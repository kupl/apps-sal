import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = dict()
    demand = 1
    pre = [0] * n
    post = [0] * n
    for i in range(n):
        d[arr[i]] = 1
        if(demand in d):
            while(demand in d):
                demand += 1
            pre[i] = demand - 1
    d2 = dict()
    # print(pre)
    demand = 1
    for i in range(n - 1, -1, -1):
        d2[arr[i]] = 1
        if(demand in d2):
            while(demand in d2):
                demand += 1
            post[i] = demand - 1
    # print(post)
    l = []
    for i in range(1, n):
        if(post[i] + pre[i - 1] == n):
            l += [[pre[i - 1], post[i]]]
    print(len(l))
    for i in l:
        print(*i)
