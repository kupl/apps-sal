def solve(s, t):
    count = 0
    a = []
    b = []
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
            a.append(s[i])
            b.append(t[i])
    if count == 0:
        return 'Yes'
    if count != 2:
        return 'No'
    if a[0] == a[1] and b[0] == b[1]:
        return 'Yes'
    return 'No'


k = int(input())
for t in range(k):
    n = int(input())
    s = input()
    t = input()
    print(solve(s, t))
