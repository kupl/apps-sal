from itertools import *
alphabet = "abcdefghijklmnopqrstuvwxyz";


def newProblem(names):
    for i in range(1, 3):
        for s in product(alphabet, repeat=i):
            st = ""
            for c in s:
                st += c
            if names.find(st) == -1:
                return st


n = int(input())
names = ""
for i in range(0, n):
    name = input()
    names += name + " "
print(newProblem(names))
