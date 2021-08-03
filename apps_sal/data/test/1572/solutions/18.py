n = int(input())
b = [int(x) for x in input().split()]
max = 2
if len(b) <= max:
    max = len(b)
s = 2
for i in range(2, len(b)):
    if b[i] == b[i - 1] + b[i - 2]:
        s += 1
    else:
        s = 2
    if s > max:
        max = s
print(max)
