n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))
num_set = set(a)


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

for b in num_set:
    lis = parse(b)
    if len(lis) < q:
        continue
    ans_tmp = sorted(lis)[q - 1] - min(lis)
    ans = min(ans, ans_tmp)

print(ans)
