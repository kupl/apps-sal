def check(a, s1, s2):
    s1, s2 = str(s1), str(s2)
    #print(s1,s2)
    #print(s1[len(s1) - len(s2):len(s1)],s2)
    #print(s1[len(s1) - len(s2):len(s1)] == s2)
    #print()
    if s1[len(s1) - len(s2):len(s1)] == s2:
        return True
    elif s1 == s2 or not(s2 in a):
        return False
        



n = int(input())
name = []
phone = []

for i in range(n):
    a = list(input().split())
    #for i in range(int(a[1]) + 1):
        #a[i + 1] = int(a[i + 1])
    if not(a[0] in name):
        name.append(a[0])
        phone.append(a[2:2 + int(a[1])])
    else:
        phone[name.index(a[0])] += a[2:2 + int(a[1])]

ans = []
for i in range(len(phone)):
    phone[i] = list(set(phone[i]))
    ans.append([])

for i in range(len(phone)):
    for j in range(len(phone[i])):
        kek = 0
        for k in range(len(phone[i])):
            if j != k and check(ans[i],phone[i][k],phone[i][j]):
                kek += 1
        if kek == 0:
            ans[i].append(phone[i][j])

print(len(name))
for i in range(len(name)):
    print(name[i], len(ans[i]), *ans[i])

