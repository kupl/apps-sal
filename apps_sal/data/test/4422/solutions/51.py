a, b = input().split()
a = int(a)
b = int(b)
c = input()
h, i, j = c[:(b - 1)], c[b - 1], c[(b):]
if i == "A":
    i = "a"
if i == "B":
    i = "b"
if i == "C":
    i = "c"
print(h + i + j)
