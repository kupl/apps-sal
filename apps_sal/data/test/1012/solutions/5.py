t = int(input())
for i in range(t):
    s = input()
    if s != s[0] * len(s):
        print(''.join(sorted(s)))
    else:
        print(-1)
