inf = 10 ** 10
input()
nums = [int(x) for x in input().split()]


def run(ns):
    curr = inf
    res = []
    for num in ns:
        if num == 0:
            curr = 0
        res.append(curr)
        curr += 1
    return res


fw = run(nums)
rew = run(reversed(nums))[::-1]
print(' '.join((str(min(fw[i], rew[i])) for i in range(len(nums)))))
