from sys import stdin
import re


def substrings(s):
    for i in range(0, len(s)):
        for l in range(i, len(s)):
            yield s[i:l + 1]


test = stdin.readline().rstrip('\n')
ruleCount = int(stdin.readline())

rules = []

for i in range(0, ruleCount):
    ruleStr = stdin.readline()
    sp = ruleStr.split(' ')

    m = {}
    for s in substrings(sp[0]):
        m[s] = m.get(s, 0) + 1

    rules.append((sp[0], int(sp[1]), int(sp[2]), m))


def works(x):
    for rule in rules:
        if not rule[1] <= rule[3].get(x, 0) <= rule[2]:
            return False

    return True


print(len([x for x in set(substrings(test)) if works(x)]))
