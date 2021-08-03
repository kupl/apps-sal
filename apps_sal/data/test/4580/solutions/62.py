N = int(input())
A = list(map(int, input().split()))
cin = [0, 0, 0, 0, 0, 0, 0, 0]
kin = 0
pin = 0
flag = 0
for i in A:
    if i < 3200:
        cin[i // 400] += 1
        pin = 1
    else:
        kin += 1
        flag = 1
if pin == 0:
    print(1, kin)
else:
    print(8 - cin.count(0), 8 - cin.count(0) + kin)
