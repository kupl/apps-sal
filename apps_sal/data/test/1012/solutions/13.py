t = int(input())
for q in range(t):
    s = sorted(list(input()))
    if s[0] == s[-1]:
        print(-1)
    else:
        print(*s, sep='')

