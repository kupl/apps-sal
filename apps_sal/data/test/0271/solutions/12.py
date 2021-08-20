from sys import stdin, stdout
n = int(stdin.readline())
if str(n)[-1] == '0':
    stdout.write(str(n))
else:
    for i in range(11):
        if str(n - i)[-1] == '0':
            stdout.write(str(n - i))
            break
        elif str(n + i)[-1] == '0':
            stdout.write(str(n + i))
            break
