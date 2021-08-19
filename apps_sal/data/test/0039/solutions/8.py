from sys import stdin, stdout
s = stdin.readline().strip()
ans = 0
for l in range(1, len(s) + 1):
    for i in range(len(s) - l + 1):
        if s[i:i + l] != s[i:i + l][::-1]:
            ans = l
stdout.write(str(ans))
