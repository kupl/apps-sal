n = int(input())
oper = list(map(int, input().split()))
rod = list(map(int, input().split()))
s = {i: [] for i in range(n)}
for i in range(len(rod)):
    s[rod[i] - 1].append(i + 1)
t = [-1] * n
t[0] = 1
black = []
grey = [0]
while grey != []:
    black.append(grey.pop())
    for i in s[black[-1]]:
        grey.append(i)
        t[i] = t[black[-1]] + 1
l = [[] for i in range(n + 1)]
for i in range(len(t)):
    l[t[i]].append(i)
l.reverse()
t = [i for i in s if s[i] == []]
ans = [1 for i in range(n)]
for i in t:
    ans[i] = -1
for x in l:
    for y in x:
        if oper[y] == 0:
            if ans[y] != 1:
                continue
            ans[y] = sum([ans[i] for i in s[y]])
        elif oper[y] == 1:
            if ans[y] != 1:
                continue
            ans[y] = max([ans[i] for i in s[y]])
t = len([i for i in s if s[i] == []])
print(t + 1 + ans[0])
