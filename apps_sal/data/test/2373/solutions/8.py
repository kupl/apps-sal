n = int(input())
p = list(map(int, input().split()))

cnt = 0
tmp = [-1, -1]
for i in range(n):
    if p[i] == i + 1:
        if i + 1 == tmp[0] + 1 and p[i] == tmp[1] + 1:
            cnt += 0
            tmp = [-1, -1]
        else:
            cnt += 1
            tmp = [i + 1, p[i]]
#    print(p[i],tmp,cnt)
print(cnt)
