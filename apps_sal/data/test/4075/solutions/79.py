(N, M) = map(int, input().split())
s = [list(map(lambda x: int(x) - 1, input().split()[1:])) for _ in range(M)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** N):
    bulb_num = 0
    for j in range(M):
        on_num = 0
        for k in range(N):
            if i >> k & 1 and k in s[j]:
                on_num += 1
        if (on_num - p[j]) % 2 == 0:
            bulb_num += 1
    if bulb_num == M:
        ans += 1
print(ans)
