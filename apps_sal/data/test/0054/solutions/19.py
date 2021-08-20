(w, m) = list(map(int, input().split()))
arr = [0] * 103
i = 0
while m != 0:
    arr[i] = m % w
    m //= w
    i += 1
for j in range(i):
    if arr[j] == 1 or arr[j] == 0:
        pass
    elif arr[j] % w == 0:
        arr[j + 1] += 1
    elif arr[j] == w - 1:
        arr[j + 1] += 1
    else:
        print('NO')
        break
else:
    print('YES')
