n = int(input())

now = 0
ans = [0] * (n)
CSF = [list(map(int, input().split())) for _ in range(n - 1)]
for i in range(n - 1):
    now = 0
    for j in range(n - i - 1):
        c, s, f = CSF[i + j]
        if now <= s:
            now = s
        else:
            now = f * ((now + f - 1) // f)
        now += c
    ans[i] = now

print(("\n".join(map(str, ans))))
