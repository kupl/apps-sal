s = input().split(' ')
l1 = int(s[0])
l2 = int(s[1])
s = input().split(' ')
a1 = s
for i in range(l1):
    a1[i] = int(a1[i])
a1.sort()
s = input().split(' ')
a2 = s
for i in range(l2):
    a2[i] = int(a2[i])
a2.sort()

for i in range(l1):
    for j in range(l2):
        if a1[i] == a2[j]:
            print(str(a1[i]))
            quit()

print(str(min(a1[0],a2[0]))+str(max(a1[0],a2[0])))
