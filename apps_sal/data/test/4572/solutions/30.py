l = set('abcdefghijklmnopqrstuvwxyz')
s = set(input())
ans = sorted(list(l ^ s))
print('None' if len(ans) == 0 else ans[0])
