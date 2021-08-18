n = int(input())
scop = []  # 高低差,min値
scom = []
ssum = 0

for i in range(n):
    s = input()
    sa = 0
    ms = 0
    for i in range(len(s)):
        if s[i] == "(":
            sa += 1
        else:
            sa -= 1
        if ms > sa:
            ms = sa
    if sa > 0:
        scop.append([ms, sa])
    elif not sa == ms:
        scom.append([ms, sa])
    ssum += sa

if not ssum == 0:
    print("No")
    return

scop.sort(reverse=True)
scom.sort()

now = 0
for i in scop:
    if now + i[0] < 0:
        print("No")
        return
    now += i[1]
for i in scom:
    if now + i[0] < 0:
        print("No")
        return
    now += i[1]

print("Yes")
