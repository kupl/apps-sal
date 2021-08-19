import copy
N = int(input())
testimony = []
for n in range(N):
    A = int(input())
    testimony.append({})
    for a in range(A):
        x, y = map(int, input().split())
        testimony[n][x - 1] = y


def judge(truthy):
    answer = True
    for i in range(len(truthy)):
        if truthy[i] == 1:
            for t in testimony[i].keys():
                if truthy[t] != testimony[i][t]:
                    answer = False
                    break
        if not answer:
            break
    # print(answer, truthy)
    return 0 if not answer else truthy.count(1)


def dfs(truthy, depth):
    if N == depth:
        return judge(truthy)
    truth = copy.copy(truthy)
    truth.append(1)
    t = dfs(truth, depth + 1)
    false = copy.copy(truthy)
    false.append(0)
    f = dfs(false, depth + 1)
    return max(t, f)


print(dfs([], 0))
