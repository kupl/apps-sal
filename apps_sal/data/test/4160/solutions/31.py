X = int(input())
kin = 100
n = 0
while kin < X:
    kin += kin// 100
    n += 1
print(n)
