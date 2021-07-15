
from sys import stdin, stdout


def write(x):
    stdout.write(str(x) + "\n")


inp = stdin.readline().strip("\n")
write(int(inp[-1])%2)


