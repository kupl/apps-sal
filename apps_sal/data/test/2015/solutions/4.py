t = int(input())
for _ in range(t):
    s = list(map(int, input().split()))
    s = sorted(s)
    if s[0] + s[1] + 1 >= s[2]:
        print('Yes')
    else:
        print('No')
