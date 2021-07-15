import copy

n, m = list(map(int, input().split()))
s = []

for i in range(m):
    st = list(map(int, input().split()))
    s.append([0]+st)


p = list(map(int, input().split()))
ans = 0

# 全bit探索
for i in range(2**(n)):
    lst = copy.deepcopy(s) # list のコピーにはcopy.copy()を用いる(2重配列以上はdeepcopy()を用いる)
    flag = True
    for j in range(n):
        if i >> j & 1 == 1:
            for k in lst:
                for l in range(2, k[1]+2):
                    if k[l]-1 == j:
                        k[0] += 1
    # 偶数奇数が合えば ans+=1
    for b in range(len(p)):
        if p[b] != lst[b][0]%2:
            flag = False
    if flag == True:
        ans +=1

print(ans)
