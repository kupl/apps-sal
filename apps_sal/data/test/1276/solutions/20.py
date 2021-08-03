from collections import Counter
from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


n = int(input())
s = input()
c = Counter(s)

ans = c['R'] * c['G'] * c['B']

lim = n // 2
for i in range(1, n // 2 + 1):
    for j in range(i, n - i):
        l = s[j - i]
        m = s[j]
        r = s[j + i]
        if l != m and m != r and r != l:
            ans -= 1

print(ans)
