"""input
4 4
abcd
"""
from sys import stdin, setrecursionlimit
import heapq
(n, p) = list(map(int, stdin.readline().split()))
string = list(stdin.readline().strip())
i = n - 1


def check_pallindrome(string, index):
    if index > 1:
        if string[index - 1] != string[index] and string[index - 2] != string[index]:
            return True
        else:
            return False
    elif index > 0:
        if string[index - 1] != string[index]:
            return True
        else:
            return False
    else:
        return True


def get_next(string, index, p):
    if ord(string[index]) - 96 < p:
        string[index] = chr(ord(string[i]) + 1)
        if check_pallindrome(string, index):
            return True
        else:
            return get_next(string, index, p)
    else:
        return False


while True:
    if i == n:
        print(''.join(string))
        break
    if i == -1:
        print('NO')
        break
    if get_next(string, i, p):
        i += 1
    else:
        string[i] = chr(96)
        i -= 1
