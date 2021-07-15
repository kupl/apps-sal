3

a = int(input())
data = list(map(int, input().split()))

c0, c1 = 0, 0

for el in data:
    if el == 1:
        c1 += 1
    else:
        c0 += 1

if (a == 1 and c0 == 0 and c1 == 1) or (a > 1 and c0 == 1):
    print("YES")
else:
    print("NO")

