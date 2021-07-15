a, b = map(int, input().split())
s = input()
l = list(input().split(" "))
mass = [0 for i in range(300)]
for i in range(b):
    mass[ord(l[i])] = 1
resm = []
p = 0
for i in range(a):
    if mass[ord(s[i])] == 1:
        p += 1
    else:
        resm += [p]
        p = 0
resm += [p]
res = 0
for i in range(len(resm)):
    res += (resm[i] * (resm[i] + 1)) // 2
print(res)
