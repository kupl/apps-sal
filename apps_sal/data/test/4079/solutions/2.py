n=int(input())
for i in range(n):
    s = ''.join(sorted(input()))
    ans = True
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i - 1]) != 1: ans = False
    if ans: print('Yes')
    else: print('No')
