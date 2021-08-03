n, m = list(map(int, input().split(' ')))
have = (n + 1) * [0]
for _ in range(m):
    person_1, person_2, owns_ = list(map(int, input().split(' ')))
    have[person_1] += owns_
    have[person_2] -= owns_

print(sum(i for i in have if i > 0))
