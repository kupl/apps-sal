(n, a, b, c) = map(int, input().split())
bamboos = []
for i in range(n):
    bamboo = int(input())
    bamboos.append(bamboo)


def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy > 0:
        out = str(X_dumy % n) + out
        X_dumy = int(X_dumy / n)
    return out


def calc_score(group, target):
    score = 0
    if len(group) > 1:
        score += 10 * (len(group) - 1)
    length = sum(group)
    score += abs(length - target)
    return score


min_score = 10 ** 12
for i in range(4 ** n):
    num = Base_10_to_n(i, 4).zfill(n)
    score = 0
    group_A = []
    group_B = []
    group_C = []
    for j in range(n):
        if num[j] == '1':
            group_A.append(bamboos[j])
        elif num[j] == '2':
            group_B.append(bamboos[j])
        elif num[j] == '3':
            group_C.append(bamboos[j])
    if len(group_A) == 0 or len(group_B) == 0 or len(group_C) == 0:
        continue
    else:
        score += calc_score(group_A, a)
        score += calc_score(group_B, b)
        score += calc_score(group_C, c)
    if score < min_score:
        min_score = score
print(min_score)
