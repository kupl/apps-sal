N = int(input())
S = input()


current = ""
ans = ""
for s in S:
    if s != current:
        current = s
        ans += s

print((len(ans)))
