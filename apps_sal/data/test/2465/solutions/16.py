T = int(input())
a = []
for i in range(3, 361):
    a.append(180 / i)

for i in range(T):
    k = int(input())
    for i in range(len(a)):
        if abs(k / a[i] - k // a[i]) < 10**-10 and k != 180 - a[i]:
            print(i + 3)
            break
