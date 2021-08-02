s = [bool(int(i)) for i in input()]
n = [bool(int(i)) for i in input()]
k = 0
a = 0
b = 0
n1 = [0]
for i in n:
    a += i
    n1.append(a)
for i in range(len(s)):
    if not s[i]:
        k += (n1[len(n) - len(s) + i + 1] - n1[i])
    else:
        k += (len(n) - len(s) + i + 1 - n1[len(n) - len(s) + i + 1] - (i - n1[i]))
print(k)
