from sys import stdin, stdout


def sin():
    return stdin.readline()


def out(s):
    stdout.write(str(s) + "\n")


a, b, c = map(int, sin().split(" "))
if ((c - a) // b) % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
