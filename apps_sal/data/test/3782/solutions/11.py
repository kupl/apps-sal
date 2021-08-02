n, k, q = map(int, input().split())
a = list(map(int, input().split()))


def parse(b):
    ret = []
    tmp = []
    for ai in a:
        if ai >= b:
            tmp.append(ai)
        else:
            if len(tmp) >= k:
                tmp.sort(reverse=True)
                for i in range(k - 1, len(tmp)):
                    ret.append(tmp[i])
            tmp = []
    else:
        if len(tmp) >= k:
            tmp.sort(reverse=True)
            for i in range(k - 1, len(tmp)):
                ret.append(tmp[i])
            tmp = []
    return ret


ans = 10**10

for b in set(a):
    lis = parse(b)
    if len(lis) < q:
        continue
    lis.sort()
    ans_tmp = lis[q - 1] - lis[0]
    ans = min(ans, ans_tmp)

print(ans)
