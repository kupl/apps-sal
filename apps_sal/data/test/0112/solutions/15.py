n = int(input().strip())
sets = [set([i for i in input().strip().split()]) for j in range(n)]


def get_all_perm(kek):
    if len(kek) == 1:
        return [kek]
    ans = []
    for i in range(len(kek)):
        p = [i for i in kek]
        p.pop(i)
        for perm in get_all_perm(p):
            ans.append([kek[i]] + perm)
    return ans


answer = 0
while answer < 10 ** n:
    answer += 1
    g = list(str(answer))
    for perm in get_all_perm(sets):
        if all([g[i] in perm[i] for i in range(len(g))]):
            break
    else:
        break
print(answer - 1)
