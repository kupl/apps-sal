inp = input()
a = inp.split()
for i in range(0, len(a)):
    a[i] = int(a[i])
time = 0
temp = 0
for i in range(0, a[0]):
    inp2 = input()
    b = inp2.split()
    b[0] = int(b[0])
    b[1] = int(b[1])
    time += b[1] - b[0] + 1 + (b[0] - temp - 1) % a[1]
    temp = b[1]
print(time)
