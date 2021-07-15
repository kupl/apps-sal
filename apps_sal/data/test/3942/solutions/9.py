c = input()  # ���� ������
count_l = 0  # ���������� (
count_r = 0  # ���������� )
h = c.count('#')
ans = [1]*h
n = len(c)

flag = 1
a = [0]*(n+1)

for i in range(n):
    if c[i] == '(':
        a[i+1] = a[i]+1
    else:
        a[i+1] = a[i]-1
    if a[i+1] < 0:
        flag = 0
        break

if flag == 0:
    print(-1)
else:
    ans[h-1] += a[n]
    pos = 0
    flag = 1
    
    for i in range(n):
        if c[i] == '(':
            count_l += 1
        elif c[i] == ')':
            count_r += 1
        else:
            count_r += ans[pos]
            pos += 1
        if count_r > count_l:
            flag = 0
            break
    
    if flag:
        for i in range(h):
            print(ans[i])
    else:
        print(-1)
