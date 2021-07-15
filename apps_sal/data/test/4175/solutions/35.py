n = int(input())
w = [input() for i in range(n)]
bool = True
for i in range(1,n):
    if w[i][0] != w[i-1][len(w[i-1]) - 1]:
        bool = False
    for j in range(0,i):
        if w[i] == w[j]:
            bool = False
if bool:
    print('Yes')
else:
    print('No')
