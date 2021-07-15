rdl1 = input()
rdl2 = input()

ans = ""
index1 = 0
index2 = 0
for i in range(len(rdl1)):
    if rdl1[i] == rdl2[i]:
        ans += rdl1[i]
    else:
        if index1 > index2:
            ans += rdl2[i]
            index2 += 1
        else:
            ans += rdl1[i]
            index1 += 1
if index1 == index2:
    print(ans)
else:
    print("impossible")

