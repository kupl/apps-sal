n = int(input())
a = reversed([int(x) for x in input().split()])
ans = -1
used = [False] * (2 * 10 ** 5 + 13)
for elem in a:
    if not used[elem]:
        used[elem] = True
        ans = elem
print(ans)
