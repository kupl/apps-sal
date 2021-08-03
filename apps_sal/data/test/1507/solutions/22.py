n, k = map(int, input().split())
s = input()
if k >= len(set(s)):
    print("NO")
    quit()
l = {}
for e in set(s):
    l[e] = len(s) - 1 - s[::-1].index(e)
g = set()
for x in range(n):
    if s[x] in g:
        if x >= l[s[x]]:
            k += 1
            g.discard(s[x])
    elif x >= l[s[x]]:
        if k > 0:
            continue
        else:
            print("YES")
            quit()
    else:
        g.add(s[x])
        k -= 1
        if k < 0:
            print("YES")
            quit()
print("YES" if k < 0 else "NO")
