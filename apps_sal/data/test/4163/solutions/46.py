N = int(input())

D1 = []
D2 = []

for i in range(N):
    a, b = list(map(int, input().split()))
    D1.append(a)
    D2.append(b)

counter = 0
flg = False

for i in range(N):
    if D1[i] == D2[i]:
        counter = counter + 1
        if counter == 3:
            flg = True
    else:
        counter = 0

if flg:
    print('Yes')
else:
    print('No')
