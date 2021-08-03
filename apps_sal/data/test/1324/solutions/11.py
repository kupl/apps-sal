import random
import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')
a = [0] * 5
ans = 0
a[1], a[2], a[3], a[4] = list(map(int, input().split()))
s = input()
for i in s:
    ans += a[ord(i) - 48]
print(ans)
