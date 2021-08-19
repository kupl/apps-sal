s = list(input())
t = s.copy()
t.reverse()
print(len(s) - t.index('Z') - s.index('A'))
