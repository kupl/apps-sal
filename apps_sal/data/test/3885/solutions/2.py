from sys import stdin, stdout


n = int(stdin.readline().rstrip())

if n%2:
    print((n-1)//2)
else:
    print(n//2 - 1)

