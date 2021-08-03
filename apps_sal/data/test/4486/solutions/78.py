S = input()
ans = ''
for i, s in enumerate(S):
    if i % 2 == 0:
        ans += s
print(ans)
