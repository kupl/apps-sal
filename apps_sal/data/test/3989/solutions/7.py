s = input()
cnt = [0] * 10
for c in s:
    cnt[int(c)] += 1
if cnt[1] == 1 and cnt[6] == 1 and (cnt[8] == 1) and (cnt[9] == 1) and (sum(cnt) == cnt[0] + 4):
    print('9618' + '0' * cnt[0])
else:
    cnt[1] -= 1
    cnt[6] -= 1
    cnt[8] -= 1
    cnt[9] -= 1
    s = []
    mod = 0
    for d in range(1, 10):
        for i in range(cnt[d]):
            s += [str(d)]
            mod *= 10
            mod += d
            mod %= 7
    import itertools
    a = [1, 6, 8, 9]
    for p in itertools.permutations(a):
        x = p[0] * 1000 + p[1] * 100 + p[2] * 10 + p[3]
        if (mod * 10000 + x) % 7 == 0:
            res = ''.join(s)
            res += str(x) + '0' * cnt[0]
            print(res)
            break
