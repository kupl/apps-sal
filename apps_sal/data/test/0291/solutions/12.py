n = [int(s) for s in input().split()]
a = n[0]
b = n[1]
t = 0
while a <= b:
    a = a*3
    b = b*2
    t += 1
print(t)

