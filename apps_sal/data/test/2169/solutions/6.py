from sys import stdin


def nii():
    return map(int, stdin.readline().split())


def lnii():
    return list(map(int, stdin.readline().split()))


(h, w, d) = nii()
a_dict = {}
for i in range(h):
    a = lnii()
    for j in range(w):
        a_dict[a[j]] = (i, j)
b_dict = {}
for i in range(1, d + 1):
    num = i
    (cy, cx) = a_dict[num]
    b_dict[num] = 0
    while num + d <= h * w:
        num += d
        (ny, nx) = a_dict[num]
        b_dict[num] = b_dict[num - d] + abs(cy - ny) + abs(cx - nx)
        cy = ny
        cx = nx
q = int(input())
for i in range(q):
    (l, r) = nii()
    ans = b_dict[r] - b_dict[l]
    print(ans)
