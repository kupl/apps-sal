import sys


def main():
    data = sys.stdin.readline().strip()
    s = set()
    for i in range(len(data)):
        for j in range(97, 123):
            s.add(data[:i] + chr(j) + data[i:])

    for j in range(97, 123):
        s.add(data + chr(j))

    print(len(s))


main()
