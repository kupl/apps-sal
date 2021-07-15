n, m = list(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))
a = b[0] * c[0]
i_k = 0
for i in range(len(b)):
    for j in range(len(c)):
        if b[i] * c[j] > a:
            a = b[i] * c[j]
            i_k = i
del b[i_k]
a = b[0] * c[0]
for i in range(len(b)):
    for j in range(len(c)):
        if b[i] * c[j] > a:
            a = b[i] * c[j]
print(a)
        

