# %%
# B
n = int(input())

found = False


def search(small, large, border):
    is_ok_l = border > int(large * (large + 1) / 2)
    is_ok_s = border > int(small * (small + 1) / 2)
    return is_ok_s, is_ok_l


width = 2 ** 16
s = 0
l = 10 ** 5

while not found:
    is_s, is_l = search(s, l, n + 1)
    if is_l and is_s:
        width = int(width * 2)
        l += width
        s += width
    elif not is_l and is_s:
        width = int(width / 2)
        l = s + width
    else:
        width = int(width / 2)
        l -= width
        s -= width
    if width < 20:
        break

k = int(s)
to = 0
while not found:
    accum = k * (k + 1) // 2
    if accum > n + 1:
        to = k - 1
        break
    elif accum == n + 1:
        to = k
        break
    k += 1

print(n - to + 1)
