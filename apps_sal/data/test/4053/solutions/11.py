import math
n = int(input())
fixes = []
for i in range(2 * n - 2):
    fixes.append(input())
fixessorted = [[] for i in range(n - 1)]
for i in fixes:
    fixessorted[len(i) - 1].append(i)
prefixes = {}
suffixes = {}
pslist = [0 for i in range(2 * n - 2)]
testprefix = fixessorted[n - 2][0]
test = 0
testsuffix = fixessorted[n - 2][1]
for i in range(0, n - 1):
    if testprefix[:n - 1 - i] in fixessorted[n - 2 - i]:
        prefixes[testprefix[:n - 1 - i]] = 1
        fixessorted[n - 2 - i].remove(testprefix[:n - 1 - i])
    else:
        test = 1
for i in range(0, n - 1):
    if testsuffix[i:] in fixessorted[n - 2 - i]:
        suffixes[testsuffix[i + 1:]] = 1
    else:
        test = 1
if test == 1:
    fixessorted = [[] for i in range(n - 1)]
    for i in fixes:
        fixessorted[len(i) - 1].append(i)
    testprefix = fixessorted[n - 2][1]
    prefixes = {}
    for i in range(0, n - 1):
        if testprefix[:n - 1 - i] in fixessorted[n - 2 - i]:
            prefixes[testprefix[:n - 1 - i]] = 1
for i in range(2 * n - 2):
    if fixes[i] in prefixes:
        pslist[i] = 'P'
        del prefixes[fixes[i]]
    else:
        pslist[i] = 'S'
print(''.join(pslist))
