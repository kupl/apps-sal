n,k = [int(i) for i in input().split()]

msg = [int(i) for i in input().split()]

fila = []
for i in msg:
    if i in fila:
        continue
    if len(fila) >= k:
        fila.pop()
    fila = [i] + fila
print(len(fila))
print(*fila)

        

