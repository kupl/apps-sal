s = input()
t = input()

ans = len(t)

for i in range(0, len(s) - len(t) + 1):
    diff = 0
    for j in range(0, len(t)):
        if t[j] != s[i + j]:
            diff += 1
    ans = min(diff, ans)


print(f"{ans}")
