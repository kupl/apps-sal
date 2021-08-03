T = int(input())
bit = []
arr = [4, 1, 3, 2, 0, 5]
s = 0
for i in range(6):
    if T % 2 == 0:
        T = T // 2
        bit.append(0)
    else:
        T = T // 2
        bit.append(1)
        s += 2**arr.index(i)
print(s)
