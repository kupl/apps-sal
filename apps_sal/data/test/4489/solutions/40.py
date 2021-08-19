N = int(input())
s = []
for i in range(N):
    s.append(input())
M = int(input())
t = []
for i in range(M):
    t.append(input())


def point(x):
    result = 0
    result += s.count(x)
    result -= t.count(x)
    return result


ans = 0
for word in set(s):
    if ans < point(word):
        ans = point(word)
print(ans)
