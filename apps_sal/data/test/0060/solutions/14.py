#import sys

#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input()
x = int(s[:len(s) - 1])
r = s[len(s) - 1]
x -= 1
kv = x // 4
ans = kv * 16
x -= kv * 4
if (x % 2 == 1):
    ans += 7
if (r == 'f'):
    ans += 1
if (r == 'e'):
    ans += 2
if (r == 'd'):
    ans += 3
if (r == 'a'):
    ans += 4
if (r == 'b'):
    ans += 5
if (r == 'c'):
    ans += 6
print(ans);

