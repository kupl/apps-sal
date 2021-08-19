arr = list(map(int, input().split()))
a = arr[0]
b = arr[1]
c = arr[2]
seq = []
for i in range(0, 2 * b):
    seq.append(a * 10 // b)
    a = a * 10 % b
if c in seq:
    print(seq.index(c) + 1)
else:
    print(-1)
