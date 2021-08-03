n = int(input())
a = list(map(int, input().split()))
now = 1
last_ind = 0
lis = []
ans = []
for i in range(n):
    if a[i] == i + 1:
        print("-1")
        return


def check(l):
    if len(l) == 0:
        return False
    now = l[0]
    for i in range(1, len(l) - 1):
        if l[i] < now:
            return False
        now = l[i]
    return True


for i in range(n):
    num = a[i]
    if num == now:
        if check(lis):
            cnt = 0
            for j in range(i, last_ind, -1):
                ans.append(j)
                lis = []
                cnt += 1
            last_ind = i
            now += cnt
        else:
            print("-1")
            return
    lis.append(num)

if len(ans) != n - 1:
    print("-1")
    return

for i in range(n - 1):
    print(ans[i])
