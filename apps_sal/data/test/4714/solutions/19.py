(a, b) = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    i = list(str(i))
    t_size = len(i)
    if t_size % 2 == 0:
        if i[:t_size // 2] == list(reversed(i[t_size // 2:])):
            ans += 1
    elif i[:t_size // 2] == list(reversed(i[t_size // 2 + 1:])):
        ans += 1
print(ans)
