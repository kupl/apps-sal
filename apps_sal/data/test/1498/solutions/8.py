n, q = [int(i) for i in input().split()]
available = [1 for i in range(n)]
for task in range(q):
    t, k , d = [int(i) for i in input().split()]    
    assign = []
    len_assign = 0
    for i in range(n):
        if available[i] <= t:
            assign.append(i)
            len_assign += 1
        if len_assign >= k:
            break
    if len_assign >= k:
        for j in range(k):
            available[assign[j]] = t+d
        print(sum(assign)+k)
    else:
        print(-1)
