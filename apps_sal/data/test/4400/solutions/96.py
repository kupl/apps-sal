S = input()
count = 0
L = []
for i in range(len(S)):
    if S[i]=='R':
        count += 1
        L.append(count)
    else:
        count = 0
        L.append(count)
print((max(L)))

