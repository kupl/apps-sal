n, k = list(map(int, input().split()))
u = list(map(int, list(input())))
if k == 0:
    print(''.join(map(str, u)))
    return
if n == 1:
    print(0)
    return
if u[0] != 1:
    u[0] = 1
else:
    k += 1
i = 1
while i < k and i < n:
    if u[i] != 0:
        u[i] = 0
    else:
        k += 1
    i += 1
print(''.join(map(str, u)))
