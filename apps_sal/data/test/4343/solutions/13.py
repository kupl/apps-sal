
n = int(input())

s1 = [ord(x) - 97 for x in input()]
s2 = [ord(x) - 97 for x in input()]

s12s = s1[n - 1] + s2[n - 1]
res = []
ni = n - 1
while ni > 0:
    ni -= 1
    s12s += (s1[ni] + s2[ni]) * 26
    res.append(chr((s12s // 2) % 26 + 97))
    s12s = s12s // 26
res.append(chr((s12s // 2) % 26 + 97))

ni = n
while ni > 0:
    ni -= 1
    print(res[ni], end='')
print()
