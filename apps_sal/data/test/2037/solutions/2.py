n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = [0 for i in range(n)]
need = 0
for i in range(m):
    a = arr[i]
    a -= 1
    if q[a] == 0:
        need += 1
    q[a] += 1
    
    if need == n:
        print(1, end='')
        for j in range(n):
            q[j] -= 1
            if q[j] == 0:
                need -= 1
    else:
        print(0, end='')

