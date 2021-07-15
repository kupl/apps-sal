n = int(input())
a = [int(s) for s in input().split()]
b = [0] * n
for i in a:
    b[i - 1] += 1

for i in b:
    print(i)
