c1 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
c3 = list(map(int,input().split()))

a1_a2 = c1[0] - c2[0]
a2_a3 = c2[0] - c3[0]
b1_b2 = c1[0] - c1[1]
b2_b3 = c1[1] - c1[2]

cnt = 0
if a1_a2 == c1[1]-c2[1] == c1[2]-c2[2]:
    cnt += 1
if a2_a3 == c2[1]-c3[1] == c2[2]-c3[2]:
    cnt += 1
if b1_b2 == c2[0]-c2[1] == c3[0]-c3[1]:
    cnt += 1
if b2_b3 == c2[1]-c2[2] == c3[1]-c3[2]:
    cnt += 1

if cnt == 4:
    print("Yes")
else:
    print("No")
