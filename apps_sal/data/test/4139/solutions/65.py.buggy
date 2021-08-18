n = int(input())

l = []


def dfs(num: list, nset: set, depth: int):
    nonlocal l
    if depth == 0:
        #print(num, nset, depth)
        if "3" in nset and "5" in nset and "7" in nset:
            l.append(int("".join(num)))
    else:
        for c in ["3", "5", "7"]:
            _num = num.copy()
            _nset = nset.copy()
            _num.append(c)
            _nset.add(c)
            dfs(_num, _nset, depth - 1)


for i in range(3, 11):
    dfs([], set(), i)

ans = 0

for i in range(len(l)):
    if n >= l[i]:
        ans += 1

print(ans)
