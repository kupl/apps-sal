s = input()
t = input()
a = list(s)
b = list(t)
j = 0
for i in range(len(b)):
    while j < len(a) and a[j] != b[i]:
        j += 1
    if j == len(a):
        break
    j += 1
else:
    print('automaton')
    return
num = [0] * 26
for x in a:
    num[ord(x) - ord('a')] += 1
for x in b:
    num[ord(x) - ord('a')] -= 1
if num == [0] * 26:
    print('array')
    return
for x in num:
    if x < 0:
        print('need tree')
        break
else:
    print('both')
