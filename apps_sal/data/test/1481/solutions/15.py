n = int(input())
i = 0
thelist = []
while i < n:
    newline = input()
    j = 0
    newlist = []
    while j < len(newline):
        newlist.append(newline[j])
        j += 1
    thelist.append(newlist)
    i += 1
finallist = []
x = 0
y = 0
row = []
while y < len(thelist) + 2:
    row.append(0)
    y += 1
finallist.append(row)
for item in thelist:
    item_0 = [0]
    for x in item:
        if x == "o":
            item_0.append(1)
        else:
            item_0.append(0)
    item_0.append(0)
    finallist.append(item_0)
finallist.append(row)
istrue = "YES"
i = 1
j = 1
while i < len(finallist) - 1:
    while j < len(finallist) - 1:
        thecount = finallist[i - 1][j] + finallist[i + 1][j] + finallist[i][j - 1] + finallist[i][j + 1]
        if thecount % 2 == 1:
            istrue = "NO"
        j += 1
    i += 1
    j = 1
print(istrue)
