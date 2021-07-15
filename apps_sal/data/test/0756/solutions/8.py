n = int(input())
t = list(map(int, input().split()))
a = [0] * 91
c = True
for e in t:
    a[e] = 1
for i in range(1, 91):
    if a[i] == 1:
        a[i] = 0
    else:
        a[i] = a[i - 1] + 1
    if a[i] == 15:
        print(i)
        c = False
        break
if c == True:
    print(90)

