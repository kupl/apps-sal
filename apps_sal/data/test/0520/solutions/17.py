from sys import stdin, stdout

n = int(stdin.readline())
years = sorted(list(map(int, stdin.readline().split())))

if n == 1:
    stdout.write(str(years[0]))
elif n == 3:
    stdout.write(str(years[1]))
elif n == 5:
    stdout.write(str(years[2]))
