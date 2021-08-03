
a, b, c = list(map(int, input().split()))
d = list()


for i in range(1, a + b):
    if a % i == 0 and b % i == 0:
        d.append(i)


sorted(d)
print((d[-c]))
