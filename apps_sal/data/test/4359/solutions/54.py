import itertools
a = [int(input()) for _ in range(5)]
cases = itertools.permutations([x for x in range(5)])
ans = 1000
for case in cases:
    time = 0
    for i in range(5):
        if time % 10 != 0:
            time += 10 - time % 10
        time += a[case[i]]
    ans = min(ans, time)
print(ans)
