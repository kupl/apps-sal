from sys import stdin, stdout
n = int(stdin.readline()) % 6
num = int(stdin.readline())
ans = [0, 1, 2]
while n > 1:
    ans = ans[1:] + [ans[0]]
    n -= 2
if n:
    (ans[0], ans[1]) = (ans[1], ans[0])
stdout.write(str(ans[num]))
