from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


(n, m) = nii()
l = [lnii() for i in range(n)]
ans = 0
for i in range(2 ** 3):
    t_l = []
    for j in l:
        t_num = 0
        for k in range(3):
            if i >> k & 1:
                t_num += j[k]
            else:
                t_num -= j[k]
        t_l.append(t_num)
    t_l.sort(reverse=True)
    ans = max(ans, sum(t_l[:m]))
print(ans)
