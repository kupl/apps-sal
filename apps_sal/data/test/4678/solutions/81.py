
N = int(input())
A = input()

Aa = A.split()

i = 0

total = 0

for i in range(N - 1):
    left = int(Aa[i])
    right = int(Aa[i + 1])

    diff = 0

    if left > right:
        diff = abs(right - left)
        total = total + diff
        Aa[i + 1] = right + diff
    else:
        total = total + 0


print(total)
