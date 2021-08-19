(n, a, b) = list(map(int, input().split()))
q = list(map(int, input().split()))
c = 0
t = True
k = 0
for i in range(n):
    if q[i] == 1 and a > 0:
        a -= 1
    elif q[i] == 1 and a == 0 and (b > 0):
        c += 1
        b -= 1
    elif q[i] == 1 and b == 0 and (a == 0) and (c > 0):
        c -= 1
    elif q[i] == 2 and b > 0:
        b -= 1
    elif q[i] == 1:
        k += 1
    else:
        k += 2
print(k)
