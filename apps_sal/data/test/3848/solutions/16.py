import sys

inf = float("inf")


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def input(): return sys.stdin.readline().strip()


def check_pallindrome(string, index):
    if index > 1:
        if string[index] != string[index - 1] and string[index] != string[index - 2]:
            return True
        else:
            return False
    elif index > 0:
        if string[index] != string[index - 1]:
            return True
        else:
            return False
    else:
        return True


def get_next(string, index, p):
    if ord(string[index]) - 96 < p:
        string[index] = chr(ord(string[index]) + 1)
        if check_pallindrome(string, index):
            return True
        else:
            return get_next(string, index, p)
    else:
        return False


n, p = get_ints()
string = list(input())
i = n - 1

while True:
    if i == n:
        print(''.join(string))
        break
    elif i == -1:
        print('NO')
        break
    if get_next(string, i, p):
        i += 1
    else:
        string[i] = chr(96)
        i -= 1
