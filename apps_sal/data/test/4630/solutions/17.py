import sys
input = sys.stdin.readline

q = int(input())

for _ in range(q):
    n = int(input())
    p = list(map(int, input().split()))
    
    for i in range(n):
        p[i] -= 1
    
    flag = [-1] * n
    ans = [-1] * n
    
    for i in range(n):
        cur = i
        
        if flag[cur] == 1:
            continue

        flag[cur] = 1
        l = [cur]
        
        while True:
            if flag[p[cur]] == 1:
                break
            
            if flag[p[cur]] == -1:
                flag[p[cur]] = 1
            
            cur = p[cur]
            l.append(cur)
        
        for li in l:
            ans[li] = len(l)
    
    print(*ans)
