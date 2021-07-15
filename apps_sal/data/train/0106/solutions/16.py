n = int(input())

for t in range(n):

    k = int(input())
    samples = []
    for i in range(k):
        samples.append(tuple(map(int, input().split())))

    samples = sorted(enumerate(samples), key=lambda x: x[1])

    tick = 1
    ans = [1]
    group_end = samples[0][1][1]

    for si in range(1, len(samples)):
        now = samples[si][1]
        if now[0] > group_end:
            tick = 2
        else:
            group_end = max(now[1], group_end)
            ans.append(1)
        if tick == 2:
            ans.extend([2] * (len(samples) - si))
            break

    ans = sorted(zip(samples, ans))
    ans = list([x[1] for x in ans])
    if 2 not in ans:
        print(-1)
    else:
        print(' '.join(map(str, ans)))


