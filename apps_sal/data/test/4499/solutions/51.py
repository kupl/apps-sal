strlist = list(map(str, input().split()))
lnum = len(strlist)

head = ""
for cnt in range(0, lnum, 1):
    head = head + (strlist[cnt][:1])
print(head.upper())
