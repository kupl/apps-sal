t = int(input())
ans = []
for i in range(t):
    n, k = [int(i) for i in input().split()]
    x = [int(i) for i in input().split()]
    max_delta = 0
    for j in range(k - 1):
        delta = x[j + 1] - x[j]
        if delta > max_delta:
            max_delta = delta
    t_ans = max(max_delta // 2 + 1, x[0], n - x[-1] + 1)
    ans.append(t_ans)
    
for a in ans:
    print(a)
