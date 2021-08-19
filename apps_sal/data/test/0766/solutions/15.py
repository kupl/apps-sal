def R():
    return list(map(int, input().split()))


s = str(input())
dyn = [0] * 26
app = [False] * 26
for i in range(len(s)):
    dyn[ord(s[i]) - ord('a')] += 1
    app[ord(s[i]) - ord('a')] = True
t = sum(app)
if t == 1 or t > 4:
    print('No')
if t == 2:
    if 1 not in dyn:
        print('Yes')
    else:
        print('No')
if t == 3:
    if max(dyn) > 1:
        print('Yes')
    else:
        print('No')
if t == 4:
    print('Yes')
