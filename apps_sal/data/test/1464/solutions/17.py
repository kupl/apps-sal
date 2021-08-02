n = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
L = []
for x in range(n):
    L.append(input())

i = 0
j = 0
k = -1
ch = alph[0]
while 1:
    if ch not in L[i]:
        i = i + 1
    else:
        j = j + 1
        if (j >= 26):
            if (j > 0) and (j % 26 == 0):
                k = k + 1
            ch = alph[k] + alph[j % 26]
        else:
            ch = alph[j]
        i = 0
    if i == n:
        break
print(ch)
