from sys import stdin, stdout


n = int(stdin.readline())
vl = list(map(int, stdin.readline().split()))
stdout.write(str(max(vl) - min(vl) + 1 - n))
