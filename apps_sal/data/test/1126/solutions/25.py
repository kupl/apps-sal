from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n, x, m = nii()

ans = x
x_list = [x]
x_table = [0 for i in range(m + 1)]
x_table[x] = 1

for i in range(1, n):
    x = (x**2) % m

    if x_table[x] != 0:
        inx = x_list.index(x)
        loop = x_list[inx:]
        zan = n - i

        p = zan // len(loop)
        q = zan % len(loop)

        ans += sum(loop) * p
        ans += sum(loop[:q])

        break

    else:
        ans += x
        x_list.append(x)
        x_table[x] += 1

print(ans)
