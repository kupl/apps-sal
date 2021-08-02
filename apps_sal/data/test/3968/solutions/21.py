def make(list):
    a, b = 0, 0
    for i in range(len(list)):
        if list[i] == 1:
            a += 1
        else:
            b += 1
    return a, b


n = int(input())
l = list(map(int, input().strip().split()))
a, b = make(l)
k = []
if b != 0:
    k.append(2)
    b -= 1
if a != 0:
    k.append(1)
    a -= 1
while b != 0:
    k.append(2)
    b -= 1
while a != 0:
    k.append(1)
    a -= 1

print(" ".join(str(x) for x in k))
