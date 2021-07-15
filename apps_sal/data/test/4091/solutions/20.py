n, k = map(int, input().split())
s = [int(elem) for elem in input().split()]
anses = []
s2 = s[:]
s2.sort(reverse = True)
s2 = s2[:k]
ans = sum(s2)
arr = []
e = 0
for i in range(n):
    if s[i] in s2:
        anses.append(str(i - e + 1))
        e = i + 1
        b = s2.index(s[i])
        del s2[b]
if e - 1 < n:
    anses[len(anses) - 1] = str(int(anses[len(anses) - 1]) + n - e)
print(ans)
print(' '.join(anses))
