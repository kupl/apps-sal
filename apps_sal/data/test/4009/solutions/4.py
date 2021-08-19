(n, x, y) = map(int, input().split())
s = input()
s = s[-x:]
cnt = 0
for i in range(len(s)):
    if i == x - y - 1 and s[i] == '0':
        cnt += 1
    elif s[i] == '1' and i != x - y - 1:
        cnt += 1
print(cnt)
