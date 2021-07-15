3

def build(n, s, t):
    ans = 1
    for i in range(n):
        if s[i] == '?' and t[i] == '?':
            ans = (55 * ans) % (10 ** 9 + 7)
        elif s[i] == '?':
            ans = ((ord(t[i]) - ord('0') + 1) * ans) % (10 ** 9 + 7)
        elif t[i] == '?':
            ans = ((ord('9') - ord(s[i]) + 1) * ans) % (10 ** 9 + 7)
    return ans


n = int(input())
s = input()
t = input()

sltt = True
tlts = True
qm = 0
cqm = 0
for i in range(n):
    if t[i] == '?':
        qm += 1
    if s[i] == '?':
        qm += 1
    if t[i] == '?' and s[i] == '?':
        cqm += 1
    if t[i] == '?' or s[i] == '?':
        continue
    if ord(s[i]) < ord(t[i]):
        tlts = False
    if ord(t[i]) < ord(s[i]):
        sltt = False


if not sltt and not tlts:
    print(pow(10, qm, 10 ** 9 + 7))
elif sltt and tlts:
    print((pow(10, qm, 10 ** 9 + 7) - build(n, s, t) - build(n, t, s) + pow(10, cqm, 10 ** 9 + 7)) % (10 ** 9 + 7))
elif sltt:
    print((pow(10, qm, 10 ** 9 + 7) - build(n, s, t)) % (10 ** 9 + 7))
else:
    print((pow(10, qm, 10 ** 9 + 7) - build(n, t, s)) % (10 ** 9 + 7))

