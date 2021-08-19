n = int(input())
fila = list(map(int, input().split()))
break_ = False
for i in range(n):
    fila[i] += i
fila = sorted(list(set(fila)))
if len(fila) < n:
    print(':(')
else:
    for j in range(n):
        fila[j] -= j
    print(' '.join(map(str, fila)))
