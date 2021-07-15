from sys import stdin as cin
from sys import stdout as cout

def main():
    n = int(cin.readline())
    if n % 4 == 0:
        print(0)
        print(n // 2, end = '')
        for i in range(n // 4):
            print('', i * 4 + 1, i * 4 + 4, end = '')
    elif n % 2 == 0:
        print(1)
        print(n // 2, end = '')
        for i in range((n - 2) // 4):
            print('', i * 4 + 1, i * 4 + 4, end = '')
        print('', n - 1)
    elif n % 4 == 1:
        print(1)
        print(n // 2, end = '')
        for i in range((n - 1) // 4):
            print('', i * 4 + 2, i * 4 + 5, end = '')
    else:
        print(0)
        print(n // 2, 3, end = '')
        for i in range((n - 3) // 4):
            print('', i * 4 + 4, i * 4 + 7, end = '')

main()

