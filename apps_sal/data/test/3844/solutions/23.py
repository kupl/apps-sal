n = int(input())
a = [int(i) for i in input().split()]
b = [0] * 200000
for i in a:
    b[i] += 1
f = 0
for i in b:
    if i % 2 == 1:
        f = 1
if f:
    print("Conan")
else:
    print("Agasa")
