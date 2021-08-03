n = list(map(int, input().split()))
N5 = 0
N7 = 0
for i in n:
    if i == 5:
        N5 += 1
    elif i == 7:
        N7 += 1
if N5 == 2 and N7 == 1:
    print("YES")
else:
    print("NO")
