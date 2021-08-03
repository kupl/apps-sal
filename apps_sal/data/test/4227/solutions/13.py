import itertools

n, m = map(int, input().split())
emp = [[] for i in range(n)]
count = 0

for i in range(m):
    a, b = map(int, input().split())
    emp[a - 1].append(b - 1)
    emp[b - 1].append(a - 1)

nlis = [i for i in range(n)]
perm = list(itertools.permutations(nlis))

for one_case in perm:
    if one_case[0] == 0:
        cou = 0
        for i in range(n - 1):
            if one_case[i + 1] in emp[one_case[i]]:
                cou += 1

            if cou == n - 1:
                count += 1
print(count)
