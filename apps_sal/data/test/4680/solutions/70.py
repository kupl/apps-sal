L = [int(i) for i in input().split()]
count5 = 0
count7 = 0
for i in range(3):
    if L[i] == 5:
        count5 += 1
    if L[i] == 7:
        count7 += 1
if count5 == 2 and count7 == 1:
    print("YES")
else:
    print("NO")
