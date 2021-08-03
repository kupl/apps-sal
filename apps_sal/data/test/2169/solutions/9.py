from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


h, w, d = nii()

a_dict = {}
for i in range(h):
    a = lnii()
    for j in range(w):
        a_dict[a[j]] = (i, j)

b_dict = {}
for i in range(1, h * w + 1):
    if i - d <= 0:
        b_dict[i] = 0
    else:
        oy, ox = a_dict[i - d]
        ny, nx = a_dict[i]
        b_dict[i] = b_dict[i - d] + abs(ny - oy) + abs(nx - ox)

q = int(input())
for i in range(q):
    l, r = nii()
    ans = b_dict[r] - b_dict[l]
    print(ans)
