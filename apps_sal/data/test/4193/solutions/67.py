li = list(map(int,input().split()))
li1 = list(map(int,input().split()))
li2 = list(map(int,input().split()))

n = int(input())
li3 = []
for i in range(n):
    li3.append(int(input()))

for i in range(3):
    if li[i] in li3:
        li[i] = 0
    if li1[i] in li3:
        li1[i] = 0
    if li2[i] in li3:
        li2[i] = 0
su = li[0] + li1[0] + li2[0]
su1 = li[1] + li1[1] + li2[1]
su2 = li[2] + li1[2] + li2[2]
su3 = li[0] + li1[1] + li2[2]
su4 = li[2] + li1[1] + li2[0]
if sum(li)==0 or sum(li1)==0 or sum(li2)==0:
    print('Yes')
elif su == 0 or su1 == 0 or su2 == 0:
    print('Yes')
elif su3 == 0 or su4 == 0:
    print('Yes')
else:
    print('No')
