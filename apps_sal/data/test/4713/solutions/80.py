a = int(input())
b = input()
c = 0
d = 0
for i in range(a):
    if b[i] == "D":
        c = c - 1
    if b[i] == "I":
        c = c + 1
    if c > d:
        d = c
print(d)
