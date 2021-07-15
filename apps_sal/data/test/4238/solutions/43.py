N = str(input())
num = list(N)
natural_num = list(map(int, num))
K = len(natural_num)
L_num = 0
for i in range(K):
    L_num += natural_num[i]
ans = L_num % 9
if ans == 0:
    print('Yes')
else:
    print('No')
