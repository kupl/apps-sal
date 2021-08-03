n = int(input())
mn = set()
otv = set()
k = 0
for i in range(ord('a'), ord('z') + 1):
    otv.add(chr(i))
for i in range(n):
    s = input().split()
    if s[0] == '!':
        otv = set(s[1]) & otv
    elif s[0] == '.':
        otv -= set(s[1])
    else:
        if i != n - 1:
            otv -= set(s[1])
    if len(otv) == 1:
        break
for bb in range(i + 1, n):
    s = input().split()
    if s[0] != '.':
        k += 1
k -= 1
if k < 0:
    k = 0
print(k)
