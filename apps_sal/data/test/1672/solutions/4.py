n = int(input())
a = []
b = ''
ot = 0
for i in range(n):
    t = input()
    if t != b:
        ot += 1
    b = t
print(ot)
