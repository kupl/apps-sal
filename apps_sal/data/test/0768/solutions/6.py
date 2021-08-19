s = input().split()
q = [0] * 10
t = int(s[1])
for i in range(int(s[0])):
    z = input()
    for j in range(t):
        if z[j] == 'Y':
            q[j] += 1
a = 0
for i in range(t):
    if q[i] >= int(s[2]):
        a += 1
print(a)
