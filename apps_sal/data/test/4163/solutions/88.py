N = int(input())
D_list = []
for i in range(N):
    s = list(map(int, input().split()))
    D_list.append(s)
a2 = D_list[0][0]
b2 = D_list[0][1]
a1 = D_list[1][0]
b1 = D_list[1][1]
for i in range(2, N):
    a0 = D_list[i][0]
    b0 = D_list[i][1]
    if a2 == b2 and a1 == b1 and a0 == b0:
        print('Yes')
        return
    a2 = a1
    b2 = b1
    a1 = a0
    b1 = b0
print('No')
