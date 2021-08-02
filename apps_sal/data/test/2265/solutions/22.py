a, b = input(), input()
t = 0
l = [0, 0]
for i in range(len(b)):
    t ^= (int(a[i]) ^ int(b[i]))
l[t] = 1
for i in range(len(b), len(a)):
    t ^= (int(a[i]) ^ int(a[i - len(b)]))
    l[t] += 1

print(l[0])
