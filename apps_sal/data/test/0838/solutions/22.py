def solution():
    ans = 0
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append([int(j) for j in input().split()])
        
    for i in range(n):
        count = 0
        for j in range(m):
            if matrix[i][j] == 1:
                count += 1
        ans += 2**count - 1
        count = m - count
        ans += 2**count - 1
    
    for j in range(m):
        count = 0
        for i in range(n):
            if matrix[i][j] == 1:
                    count += 1
        
        if count > 1:
            ans += 2**count - 1 - count
        
        count = n - count
        if count > 1:
            ans += 2**count - 1 - count
    print(ans)
    
solution()
