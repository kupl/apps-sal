import itertools
n, k = list(map(int, input().split()))
list_S = list(input())

list_N = []
gr = itertools.groupby(list_S)
cnt = 0

for key, group in gr:
    list_N.append([key, len(list(group))])
    if key == "0":
        cnt += 1

if cnt <= k:
    print(n)
else:
    if list_N[0][0] == "0":
        list_N.insert(0, ["1", 0])
    if list_N[-1][0] == "0":
        list_N.append(["1", 0])

    s = 0
    for i in range(2 * k + 1):
        s += list_N[i][1]
    ans = s

    for i in range(2 * k + 2, len(list_N), 2):
        s += list_N[i][1] + list_N[i - 1][1] - list_N[i - 2 * k - 2][1] - list_N[i - 2 * k - 1][1]
        ans = max(ans, s)

    print(ans)

