def count(s):
    c = [0] * 26
    for t in s:
        c[ord(t) - ord('a')] += 1
    return c


c1 = count(input())
c2 = count(input())
valid = True
result = 0
for i in range(26):
    if c2[i] > 0 and c1[i] == 0:
        valid = False
    result += min(c1[i], c2[i])
if not valid:
    print(-1)
else:
    print(result)
