alth = 'abcdefghijklmnopqrstuvwxyz'
alth2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s2 = [[0] * 26 for i in range(2)]
s3 = [[0] * 26 for i in range(2)]
s = input()
t = input()
num = 0
num2 = 0
for i in s:
    temp = alth.find(i)
    if temp != -1:
        s2[0][temp] += 1
    temp = alth2.find(i)
    if temp != -1:
        s2[1][temp] += 1
for i in t:
    temp = alth.find(i)
    if temp != -1:
        s3[0][temp] += 1
    temp = alth2.find(i)
    if temp != -1:
        s3[1][temp] += 1
for i in range(2):
    for j in range(26):
        x = min(s2[i][j], s3[i][j])
        num += x
        s2[i][j] -= x
        s3[i][j] -= x
for i in range(2):
    for j in range(26):
        num2 += min(s2[i][j], s3[1 - i][j])
print(num, num2)
