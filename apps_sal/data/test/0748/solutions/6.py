n = int(input())
a = list(map(int, input().split()))
b = [0] * 8
h = []
for i in a:
    b[i] += 1
v = min(b[1], b[2], b[4])
b[1] -= v
b[2] -= v
b[4] -= v
h.append(v)

v = min(b[1], b[3], b[6])
b[1] -= v
b[3] -= v
b[6] -= v
h.append(v)

v = min(b[1], b[2], b[6])
b[1] -= v
b[2] -= v
b[6] -= v
h.append(v)

if sum(h) * 3 < n:
    print(-1)
else:
    print('1 2 4 \n' * h[0], end = '')
    print('1 3 6 \n' * h[1], end = '')
    print('1 2 6 \n' * h[2], end = '')
    

    
    
