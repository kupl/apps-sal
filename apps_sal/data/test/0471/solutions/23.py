(n, a) = map(int, input().split())
N = sorted(list(map(int, input().split())))
dist = 0
if n == 1:
    dist = 0
elif n == 2:
    dist = min(abs(N[0] - a), abs(N[1] - a))
elif a <= N[0]:
    dist = abs(N[-2] - a)
elif a >= N[-1]:
    dist = abs(a - N[1])
elif a >= N[-2]:
    dist = min(abs(a - N[0]), 2 * abs(a - N[-1]) + abs(a - N[1]), abs(a - N[-1]) + 2 * abs(a - N[1]))
elif a <= N[1]:
    dist = min(abs(a - N[-1]), 2 * abs(a - N[0]) + abs(a - N[-2]), abs(a - N[0]) + 2 * abs(a - N[-2]))
else:
    dist = min(2 * abs(N[0] - a) + abs(N[-2] - a), 2 * abs(N[1] - a) + abs(N[-1] - a), 2 * abs(N[-1] - a) + abs(N[1] - a), 2 * abs(N[-2] - a) + abs(N[0] - a))
print(dist)
