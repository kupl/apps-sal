(a, b) = input().split()
a = int(a)
b = int(b)
c = list(map(int, input().split()))
d = 0
e = 0
for i in range(a):
    if d + c[i] <= b:
        d = d + c[i]
        e = e + 1
    else:
        break
print(e + 1)
