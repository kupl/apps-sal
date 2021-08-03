from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, k = nii()
a = lnii()

x = 0
x_list = [1]
x_table = [0 for i in range(n + 1)]
x_table[1] = 1

for i in range(k):
    nx = a[x]

    if x_table[nx] != 0:
        inx = x_list.index(nx)
        loop = x_list[inx:]
        zan = k - i

        q = zan % len(loop)

        nx = loop[q - 1]
        break

    else:
        x = nx - 1
        x_list.append(nx)
        x_table[nx] += 1

print(nx)
