s = input()
t = input()
ans = 0
for (s, t) in zip(s, t):
    if s != t:
        ans += 1
print(ans)
