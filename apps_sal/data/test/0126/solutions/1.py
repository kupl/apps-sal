n = int(input())
numb = input()
num = [0]*10
for i in numb:
    num[int(i)] = 1
ans = 0
if num[1] + num[2] + num[3] > 0:
    ans += 1
if num[1] + num[4] + num[7] + num[0] > 0:
    ans += 1
if num[3] + num[6] + num[9] + num[0] > 0:
    ans += 1
if num[7] + num[0] + num[9] > 0:
    ans += 1
if ans == 4:
    print("YES")
else:
    print("NO")

