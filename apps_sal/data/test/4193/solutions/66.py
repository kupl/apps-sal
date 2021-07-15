a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
n = int(input())
flag = 0
for _ in range(n):
    b = int(input())
    for i in range(3):
        if b == a1[i]:
            a1[i] = 0
        elif b == a2[i]:
            a2[i] = 0
        elif b == a3[i]:
            a3[i] = 0
    for i in range(3):
        if a1[i] == a2[i] == a3[i]:
            flag = 1
        if sum(a1) == 0:
            flag = 1
        if sum(a2) == 0:
            flag = 1
        if sum(a3) == 0:
            flag = 1
        if a1[0] == a2[1] == a3[2]:
            flag = 1
        if a1[2] == a2[1] == a3[0]:
            flag = 1
    if flag == 1:
        print("Yes")
        break
if flag == 0:
    print("No")
