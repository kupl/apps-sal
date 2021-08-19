from itertools import *
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def isValid(s, names):
    for name in names:
        if name.find(s) != -1:
            return False
    return True


def newProblem(names):
    for i in range(1, 3):
        for s in product(alphabet, repeat=i):
            st = ''
            for c in s:
                st += c
            if isValid(st, names):
                return st


n = int(input())
names = []
for i in range(0, n):
    name = input()
    names.append(name)
print(newProblem(names))
