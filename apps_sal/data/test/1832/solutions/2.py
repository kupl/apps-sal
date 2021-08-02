def nxt(ch):
    if ch == 'z':
        return 'a'
    return chr(ord(ch) + 1)


ans = []
for _ in range(int(input())):
    n = int(input())
    u = list(map(int, input().split()))
    s = ['a']
    for i in range(51):
        s.append(nxt(s[-1]))
    ans.append(''.join(s))
    for i in range(n):
        s[u[i]] = nxt(s[u[i]])
        ans.append(''.join(s))
print('\n'.join(ans))
