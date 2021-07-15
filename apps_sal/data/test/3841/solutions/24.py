p, k = list(map(int, input().split()))
arr = []
while p:
    a, b = divmod(p, -k)
    if b < 0:
        a += 1
        b += k
    p = a
    arr.append(str(b))
print(len(arr))
print(' '.join(arr))

