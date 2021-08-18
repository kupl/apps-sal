s = input()
t = input()

"""pos=[]
for i in range(26):
    h=[]
    pos.append(h)

for i in range(0,len(t)):
    for j in range(0,len(s)):
        if(s[j]==t[i]):
            pos[i].append(j)"""

L1 = []
L2 = []

ptr = 0
for i in range(0, len(s)):
    if(s[i] == t[ptr]):
        L1.append(i)
        ptr += 1
    if(ptr >= len(t)):
        break

ptr = len(t) - 1
for i in range(len(s) - 1, -1, -1):
    if(s[i] == t[ptr]):
        L2.append(i)
        ptr -= 1
    if(ptr < 0):
        break

L2 = L2[::-1]


mx = -1
for i in range(0, len(L1) - 1):
    mx = max(mx, L2[i + 1] - L1[i] - 1)

mx = max(mx, L2[0])
mx = max(mx, len(s) - L1[-1] - 1)

print(mx)
