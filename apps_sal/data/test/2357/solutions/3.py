# [t0, ... tn-1] dominerad av V: minst 2 element
# occ(num) förekomster av num i t
# occ(v) > occ(v') -- när v förekommer flest gånger och inget annat förekommer lika många gånger.
# kortaste dominerade dellista (slice, sammanhängande).

# 4 <- T

# 1
# 1 (jaha, minst längd 2)

# 6
# 1 2 3 4 5 1 - hela grejen har 2 ettor

# 9
# 4 1 2 4 5 4 3 2 1 - 4 5 4 har 2 fyror

# 4
# 3 3 3 3 - 3 3 har 2 treor

# OK N^3-algoritm - enkelt - aha, det räcker med att hitta 2 likadana element och olika mellan.
# För varje x - lista var alla förekomster är. gå igenom alla och hitta närmaste.

import collections


def sol(lst):
    d = collections.defaultdict(list)
    for i, x in enumerate(lst):
        d[x].append(i)

    MIN_SOL = 10**10
    for x in d:
        for a, b in zip(d[x], d[x][1:]):
            MIN_SOL = min(MIN_SOL, b - a + 1)
    if MIN_SOL == 10**10:
        print(-1)
    else:
        print(MIN_SOL)


t = int(input())
for _ in range(t):
    _ = int(input())
    sol([int(x) for x in input().split()])
