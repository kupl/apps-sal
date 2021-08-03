s = input()
N = len(s)
ans = 0
for c in s:
    if c == "p":
        ans -= 1
ans += N // 2
print(ans)
