n, h = map(int, input().split())
a, b = map(int, input().split())
L = [[a, b]]
M = [0]
N = [0]
sum = 0
f = True
for i in range(1, n):
    a, b = map(int, input().split())
    L.append([a, b])
    M.append(a - L[-2][1])
    sum += M[-1]
    if sum >= h and f:
        x = i 
        f = False
    N.append(sum)
if sum < h:
    maximum = L[-1][1] - L[0][0] + h - sum
else:
    #print('x =', x)
    ans = L[x - 1][1] - L[0][0] + h - N[x - 1]
    maximum = ans
    for i in range(1, n):
        while x < n and N[x] - N[i] < h:
            x += 1
        ans = L[x - 1][1] - L[i][0] + h - (N[x - 1] - N[i])
        if ans > maximum:
            maximum = ans
        #print('i =', i, 'x =', x, 'ans =', ans)
print(maximum)
