
a = len(input()[2:])
b = len(input()[2:])
c = len(input()[2:])
d = len(input()[2:])

arr = [a, b, c, d]

candi = []
for i, x in enumerate(arr):
    sf = True
    bf = True
    for j, y in enumerate(arr):
        if i != j:
            if x > y / 2:
                sf = False
            if x < y * 2:
                bf = False
    if sf or bf:
        candi.append(i)

if len(candi) == 1:
    print(chr(ord('A') + candi[0]))
else:
    print("C")
