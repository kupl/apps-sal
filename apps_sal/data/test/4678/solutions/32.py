n = int(input())
s = 0
x = list(map(int, input().split()))
z = x[0]
for i in range(len(x)):
    if z > x[i]:
        s += z - x[i]
    else:
        z = x[i]
print(s)
