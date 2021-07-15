import sys
input = sys.stdin.readline

s = input()
ans = 0
for i in range(4):
    if s[i] == '+':
        ans += 1
    else:
        ans -= 1
print(ans)
