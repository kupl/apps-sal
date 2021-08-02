alth = "abcdefghijklmnopqrstuvwxyz"
alth2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
t = input()
num3 = [0] * 26
for i in t:
    if alth.find(i) != -1:
        num3[alth.find(i)] = 1
    elif alth2.find(i) != -1:
        num3[alth2.find(i)] = 1
if sum(num3) == 26:
    print("YES")
else:
    print("NO")
