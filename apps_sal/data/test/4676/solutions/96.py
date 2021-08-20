o = list(input())
e = list(input()) + ['']
ans = ''.join((o + e for (o, e) in zip(o, e)))
print(ans)
