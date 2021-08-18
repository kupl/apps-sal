import sys
x1, y1, x2, y2, x3, y3 = map(int, input().split())

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)


for i in range(2):
    for j in range(2):
        for k in range(2):
            if a[i] == b[j] == c[k] and a[1 - i] + b[1 - j] + c[1 - k] == a[i]:
                print(a[i])
                print(("A" * a[i] + "\n") * a[1 - i], end="")
                print(("B" * b[j] + "\n") * b[1 - j], end="")
                print(("C" * c[k] + "\n") * c[1 - k], end="")

               # print(i, j, k)
                return


r = max(max(a), max(b), max(c))

xs = [a, b, c]


for i, t in enumerate(xs):
    if r == max(t):
        index = i
        break

o = xs[index][:]

s = o[1] if o[0] == r else o[0]
del xs[index]

for i in range(2):
    for j in range(2):
        if (xs[0][i] == xs[1][j] == r - s and xs[0][1 - i] + xs[1][1 - j] == r):
            print(r)
            symb = chr(ord("A") + index)
            print((symb * r + "\n") * s, end="")
            syms = ["A", "B", "C"]
            syms.remove(symb)
            print((syms[0] * xs[0][1 - i] + syms[1] * xs[1][1 - j] + "\n") * (r - s), end="")
            return
# print(r)
# not possible, return - 1


print(-1)
