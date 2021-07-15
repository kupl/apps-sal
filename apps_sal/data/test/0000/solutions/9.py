def ii():
    return int(input())
def mi():
    return list(map(int, input().split()))
def li():
    return list(mi())

s = input().strip()
n = len(s)
ans = -1
fb = s.find('[')
if fb >= 0:
    fc = s.find(':', fb)
    if fc >= 0:
        lb = s.rfind(']')
        if lb > fc:
             lc = s.rfind(':', 0, lb)
             if lc > fc:
                ans = 4 + s[fc:lc].count('|')
print(ans)

