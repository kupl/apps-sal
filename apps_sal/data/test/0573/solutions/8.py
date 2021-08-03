n = int(input())
a = list(map(int, input().split()))
c = [0, 0]
for i in a:
    if i == 1:
        c[0] += 1
    else:
        c[1] += 1

if c[1] < c[0]:
    print(c[1] + (c[0] - c[1]) // 3)
else:
    print(c[0])
