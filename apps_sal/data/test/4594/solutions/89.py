N=int(input())
D = []
for _ in range(N):
    d = int(input())
    D.append(d)

D_num=list(set(D))
print(len(D_num))
