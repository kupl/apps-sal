n, m = list(map(int, input().split()))

s = ''

def rr(n, m, i, j):
    if j == 0:
        if 2*i + 1 <= m:
            return 2*i + 1
        else:
            return 0
    elif j == 1:
        if 2*n + 2*i + 1 <= m:
            return 2*i + 2*n + 1
        else:
            return 0
    elif j == 2:
        if 2*i + 2 + 2*n <= m:
            return 2*i + 2 + 2*n
        else:
            return 0
    else:
        if 2*i + 2 <= m:
            return 2*i + 2
        else:
            return 0

for i in range(n):
    for j in 1, 0, 2, 3:
        a = rr(n, m, i, j)
        if a != 0:
            s += str(a) + ' '

print(s)
       
    

