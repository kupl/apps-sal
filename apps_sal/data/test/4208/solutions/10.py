n = int(input())
l = input()
r = input()
li = [0] * 27
li2 = [[] for i in range(27)]
ri = [0] * 27
ri2 = [[] for i in range(27)]
alth = "qwertyuiopasdfghjklzxcvbnm?"
for i in range(n):
    i1 = alth.find(l[i])
    i2 = alth.find(r[i])
    li[i1] += 1
    ri[i2] += 1
    li2[i1] += [i]
    ri2[i2] += [i]
    
for i in range(27):
    li2[i] += [len(li2[i]) - 1]
    ri2[i] += [len(ri2[i]) - 1]

ans = [0] * n
num = 0
for i in range(26):
    while li2[i][-1] > -1 and ri2[i][-1] > -1:
        ans[num] = [li2[i][li2[i][-1]],ri2[i][ri2[i][-1]]]
        num += 1
        li2[i][-1] -= 1
        ri2[i][-1] -= 1
        
for i in range(26):
    while li2[i][-1] > -1 and ri2[-1][-1] > -1:
        ans[num] = [li2[i][li2[i][-1]],ri2[-1][ri2[-1][-1]]]
        num += 1
        li2[i][-1] -= 1
        ri2[-1][-1] -= 1

for i in range(26):
    while li2[-1][-1] > -1 and ri2[i][-1] > -1:
        ans[num] = [li2[-1][li2[-1][-1]],ri2[i][ri2[i][-1]]]
        num += 1
        li2[-1][-1] -= 1
        ri2[i][-1] -= 1
while li2[-1][-1] > -1 and ri2[-1][-1] > -1:
        ans[num] = [li2[-1][li2[-1][-1]],ri2[-1][ri2[-1][-1]]]
        num += 1
        li2[-1][-1] -= 1
        ri2[-1][-1] -= 1
print(num)
for i in range(num):
    print(ans[i][0] + 1, ans[i][1] + 1)

