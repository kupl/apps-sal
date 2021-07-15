n, p = list(map(int, input().split()))
e = []
for i in range(n):
    l, r = list(map(int, input().split()))
    L = -1
    R = 10 ** 9 + 7
    while L != R - 1:
        m = (L + R) // 2
        if m * p < l:
            L = m
        else:
            R = m
    col1 = R
    L = -1
    R = 10 ** 9 + 7
    while L != R - 1:
        m = (L + R) // 2
        if m * p <= r:
            L = m
        else:
            R = m
    col2 = R
    col = r - l + 1
    e.append(1 - (col2 - col1) / col)
sum = 0
for i in range(n):
    sum += 1000 * (1 - (e[i] * e[i - 1]))
print(sum * 2)

       
    
        

