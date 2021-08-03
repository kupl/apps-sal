m, k = map(int, input().split())
if m == 1:
    if k != 0:
        print(-1)
    else:
        print(0, 0, 1, 1)
    return
elif 2**m <= k:
    print(-1)
    return
b = []
for i in range(2**m):
    if i != k:
        b.append(i)
c = b[::-1]
d = b + [k] + c + [k]
print(*d)
