s = input()
t = input()

ls = len(s)
lt = len(t)
check = False
ans = 'z'*60
for i in range(ls-lt+1):
    u = list(s)
    flag = True
    for j in range(lt):
        if u[i+j] == '?':
            u[i+j] = t[j]
        elif u[i+j] != t[j]:
            flag = False
            break
    if flag:
        check = True
        u = ''.join(u).replace('?', 'a')
        ans = sorted([ans, u])[0]
print(ans if check else 'UNRESTORABLE')
