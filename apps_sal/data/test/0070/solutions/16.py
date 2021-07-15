from sys import stdin, stdout


s, k = stdin.readline().split()
k = int(k)

ans = 0
cnt = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] != '0':
        ans += 1
    elif s[:i + 1].count('0') != len(s[:i + 1]):
        cnt += 1
    
    if cnt == k:
        stdout.write(str(ans))
        break
else:
    stdout.write(str(len(s) - 1))
