N = int(input())
d_lst = []
D_lst = []
cnt = 0
for i in range(N):
    d = int(input())
    d_lst.append(d)

for j in range(max(d_lst)+1):
    D = d_lst.count(j)
    D_lst.append(D)
    if D == 0:
        pass
    else:
        cnt += 1
print(cnt)
