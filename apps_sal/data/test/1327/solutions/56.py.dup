from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, m = nii()
l = [lnii() for i in range(n)]

ans = 0
for i in [1, -1]:
    for j in [1, -1]:
        for k in [1, -1]:
            t_num = 0
            t_l = []
            for x, y, z in l:
                t_num = x * i + y * j + z * k
                t_l.append(t_num)
            t_l.sort(reverse=True)
            ans = max(ans, sum(t_l[:m]))

print(ans)
