import sys
def input(): return sys.stdin.readline().strip()


def opp(s):
    if s == 'a':
        return 'b'
    else:
        return 'a'


n = int(input())
s = list(input())
cnt = 0
for i in range(0, n, 2):
    if s[i] != opp(s[i + 1]):
        cnt += 1
        s[i] = opp(s[i + 1])
print(cnt)
print(''.join(s))
