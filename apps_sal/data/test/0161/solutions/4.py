x = int(input())

ans = []

cnt = 0

while x & (x + 1) != 0:
    bn = str(bin(x)[2:])
    cnt += 1

    ret = -1
    for i in range(len(bn)):
        if bn[i] == '0':
            ret = i
            break

    if ret == -1:
        break

    x ^= 2 ** (len(bn) - ret) - 1
    ans.append(len(bn) - ret)

    if x & (x + 1) == 0:
        break

    x += 1
    cnt += 1

print(cnt)
if len(ans) > 0:
    print(' '.join(str(el) for el in ans))
