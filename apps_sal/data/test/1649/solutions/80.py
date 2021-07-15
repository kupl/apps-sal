from itertools import product
a = list(map(int, input().split()))
s = sum(a)
for bit in product([0, 1], repeat=4):
    tmp = 0
    for i, j in enumerate(bit):
        if j == 1:
            tmp += a[i]
    if tmp == s - tmp:
        print("Yes")
        return
print("No")
