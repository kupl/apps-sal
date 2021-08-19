sum1 = 0


def gen(used, pref, m, ans):
    if len(pref) == n:
        ans.append(pref)
    else:
        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                gen(used, pref + [i], m, ans)
                used[i] = False


n, m = map(int, input().split())
used = [False] * (n + 1)
ans = []
gen(used, [], m, ans)
min1 = -1
mm = -1
summ = [0] * len(ans)
for i in range(len(ans)):
    sum1 = 0
    for z in range(n):
        for j in range(z, n):
            sum1 += min(ans[i][z:j + 1])
    summ[i] = sum1
    if sum1 >= min1:
        min1 = sum1
        mm = i
ss = 0
i = 0
while ss <= m:
    #print(i, ss)
    if summ[i] < min1:

        #print(i, ss, 1)
        i += 1
    else:
        if summ[i] == min1:
            if ss == m - 1:
                break
            #print(i, ss, 2)
            ss += 1
            i += 1
# print(i)
print(' '.join(map(str, ans[i])))
