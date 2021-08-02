import itertools


v1, v2 = list(map(int, str.split(input())))
t, d = list(map(int, str.split(input())))

cv = v1
s = v1 + v2
steps = list(itertools.accumulate((v1,) + tuple(range(2, t)), lambda x, _: x + d)) + [v2]
for i in range(t - 1, -1, -1):

    if steps[i - 1] - steps[i] > d:

        steps[i - 1] = steps[i] + d

    else:

        break

print(sum(steps))
