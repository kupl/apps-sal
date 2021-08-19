num = input()
res = '-1'
l = len(num)
a = int(num[l - 1])
n = []
for i in range(l):
    n.append(num[i])
flag = 1
i = 0
while flag and i < l:
    if int(num[i]) % 2 == 0 and int(num[i]) < a:
        n[l - 1] = n[i]
        n[i] = str(a)
        flag = 0
        s = ''.join(n)
        res = s
    i += 1
i = l - 1
while flag and i >= 0:
    if int(num[i]) % 2 == 0:
        n[l - 1] = n[i]
        n[i] = str(a)
        flag = 0
        s = ''.join(n)
        res = s
    i -= 1
print(res)
