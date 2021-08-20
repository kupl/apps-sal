from sys import stdin
lines = list([_f for _f in stdin.read().split('\n') if _f])


def parseline(line):
    return list(map(int, line.split()))


lines = list(map(parseline, lines))
(n,) = lines[0]
a = lines[1]
(m,) = lines[2]
b = lines[3]
assert len(a) == n and len(b) == m
Max = 100 + 1
ai_count = [0] * Max
bi_count = [0] * Max
for ai in a:
    ai_count[ai] += 1
for bi in b:
    bi_count[bi] += 1
match = [[] for i in range(Max)]
used = None


def dfs(v):
    if used[v] >= ai_count[v]:
        return False
    used[v] += 1
    for to in range(max(0, v - 1), min(Max, v + 2)):
        if len(match[to]) < bi_count[to]:
            match[to].append(v)
            return True
        for (i, to_i) in enumerate(match[to]):
            if dfs(to_i):
                match[to][i] = v
                return True
    return False


for i in range(Max):
    for _ in range(ai_count[i]):
        used = [0] * Max
        dfs(i)
print(sum((len(l) for l in match)))
