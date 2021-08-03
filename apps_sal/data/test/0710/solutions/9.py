n = int(input())
s = input()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def make(a, b):
    if ord(b) < ord(a):
        a, b = b, a
    return min(ord(b) - ord(a), ord('Z') - ord(b) + ord(a) - ord('A') + 1)


def change(x):
    final = 'ACTG'
    ans = 0
    c = 0
    for i in x:
        ans += make(i, final[c])
        c += 1
    return ans


ans = 10**5

for i in range(n):
    if i + 3 < n:
        cur = s[i:i + 4]
        ans = min(ans, change(cur))
print(ans)
