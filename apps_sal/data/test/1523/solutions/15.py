(n, k) = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
ans = dict()
rem = []
for i in range(n):
    if alist[i] in ans:
        if blist[i] > ans[alist[i]]:
            rem += [ans[alist[i]]]
            ans[alist[i]] = blist[i]
        else:
            rem += [blist[i]]
    else:
        ans[alist[i]] = blist[i]
srem = sorted(rem)
index = 0
answer = 0
for i in range(1, k + 1):
    if not i in ans:
        answer += srem[index]
        index += 1
print(answer)
