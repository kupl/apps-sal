from sys import stdin as cin
from sys import stdout as cout


def main():
    s = cin.readline()
    o = 0
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7', '9']:
            o += 1
    print(o)


main()
