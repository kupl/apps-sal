a = input()
v = [''] * 4
s = [0] * 4
for i in range(len(a)):
    if(i % 4 == 0):
        if(a[i] != '!'):
            v[i % 4] = a[i]
    if(i % 4 == 1):
        if(a[i] != '!'):
            v[i % 4] = a[i]
    if(i % 4 == 2):
        if(a[i] != '!'):
            v[i % 4] = a[i]
    if(i % 4 == 3):
        if(a[i] != '!'):
            v[i % 4] = a[i]
for i in range(len(a)):
    if(a[i] == '!'):
        if(v[i % 4] == "R"):
            s[0] += 1
        if(v[i % 4] == "B"):
            s[1] += 1
        if(v[i % 4] == "Y"):
            s[2] += 1
        if(v[i % 4] == "G"):
            s[3] += 1
for i in range(4):
    print(s[i], end=" ")
