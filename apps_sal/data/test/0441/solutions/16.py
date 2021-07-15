t = input().split(' ')
n = int(t[0])
a = int(t[1])
b = int(t[2])
s = input()
L = [0] * len(s)
for i in range(len(s)):
    if s[i] == '.':
        L[i] = 1
M = [0] + L + [0]
c = True
d = False
tot = 0
for j in range(1, len(s)+1):
    if M[j] == 1 and M[j-1] != 2 and a > 0:
        c = True
    else:
        c = False
    if M[j] == 1 and M[j-1] != 3 and b > 0:
        d = True
    else:
        d = False
    if c and d:
        if a > b:
            d = False
        else:
            c = False
    if c and not d:
        M[j] = 2
        a -= 1
        tot += 1
    if d and not c:
        M[j] = 3
        b -= 1
        tot += 1
print(tot)

