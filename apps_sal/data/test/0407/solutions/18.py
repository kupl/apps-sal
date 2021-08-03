b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
l = [0] * 10
z = set()
n = int(input())
for i in range(n):
    s = input()
    z.add(s[0])
    for j in range(len(s)):
        l[b.index(s[j])] += 10**(len(s) - j - 1)
s = 0
h = 0
j = 1
notfirst = set(b) - z
for k in range(10):
    ma = 0
    value = 0
    for i in range(10):
        if l[i] > ma:
            ma = l[i]
            value = i
    if(b[value] in z) or h == 1:
        s += ma * j
        j += 1
    else:
        h = 1
    l[value] = 0
print(s)
