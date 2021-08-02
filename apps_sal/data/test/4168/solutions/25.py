def mod(i, j):
    if i % j == 0:
        return [str(0), i // j]
    else:
        return [str(-(i % j)), (i // j) + 1]


n = int(input())
w = ""
if n == 0:
    w = 0
else:
    while n != 0:
        i, j = mod(n, -2)
        w = i + w
        n = j
print(w)
