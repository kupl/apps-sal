import numpy as np

H, W, K = list(map(int, input().split()))
cmap = []
for i in range(H):
    tmp = input()
    strlist = [s for s in tmp]
    cmap.append(strlist)

cmap = np.array(cmap)


def count_char(cmap, rmask, cmask, num_digits_r, num_digits_c, char="#"):
    def to_bin_str(num, num_digits):
        return str(bin(num))[2:].zfill(num_digits)

    def to_index(mask, num_digits):
        str = to_bin_str(mask, num_digits)
        ids = [i for i, s in enumerate(str) if s == "1"]
        return ids

    rids = to_index(rmask, num_digits_r)
    cids = to_index(cmask, num_digits_c)
    cmap2 = cmap.copy()
    cmap2[rids, :] = "r"
    cmap2[:, cids] = "r"
    count = len(cmap2[cmap2 == char])

    # if count == K:
    #     print(cmap2)

    return count


count = 0
for rmask in range(2**H):
    for cmask in range(2**W):
        num_b = count_char(cmap, rmask, cmask, H, W)
        if num_b == K:
            count += 1

print(count)

