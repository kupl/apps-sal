n = int(input())
l = list(map(int, input().split()))

l = [0] + l

pos = [0] * (n + 1)
for i in range(n + 1):
    pos[l[i]] = i

ans = []
flag = True
tmp = n
while tmp > 1:
    ind = pos[tmp]
    if ind < tmp:
        for i in range(ind + 1, tmp):
            if l[i + 1] != i:
                flag = False
                break
            pos[l[i - 1]], pos[l[i]] = i, i - 1
            l[i - 1], l[i] = l[i], l[i - 1]
            ans.append(i - 1)
        if flag:
            pos[l[tmp - 1]], pos[l[tmp]] = tmp, tmp - 1
            l[tmp - 1], l[tmp] = l[tmp], l[tmp - 1]
            ans.append(tmp - 1)
            tmp = ind
        else:
            break
    else:
        flag = False
        break

if flag:
    for ele in ans:
        print(ele)
else:
    print(-1)
