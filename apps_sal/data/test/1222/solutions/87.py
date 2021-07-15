k = int(input())
ans = []


def gen_lunlun(x):
    if x <= 3234566667:
        d = x % 10
        for i in [-1, 0, 1]:
            if d + i < 0 or d + i >= 10:
                continue
            nex = x * 10 + d + i
            ans.append(nex)
            gen_lunlun(nex)


for i in range(1, 10):
    ans.append(i)
    gen_lunlun(i)
ans = sorted(ans)

print((ans[k - 1]))

