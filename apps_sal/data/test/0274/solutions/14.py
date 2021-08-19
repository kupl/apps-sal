n = input()
s = input()
bal = []
curbal = 0
maxbal = 0
for i in s:
    if i == '[':
        bal.append((curbal, 1))
        curbal += 1
        maxbal = max(curbal, maxbal)
    else:
        bal.append((curbal, -1))
        curbal -= 1
bal = [(maxbal - i, j) for (i, j) in bal]
stack = []
ans = [[] for _ in range(2 * maxbal + 1)]
for i in range(len(bal)):
    if bal[i][1] == 1:
        stack.append(bal[i][0])
        if i == 0 or bal[i - 1][1] == 1:
            for j in range(maxbal - bal[i][0]):
                ans[j].append(' ')
            ans[maxbal - bal[i][0]].append('+-')
            for j in range(maxbal - bal[i][0] + 1, maxbal + bal[i][0]):
                ans[j].append('|')
            ans[maxbal + bal[i][0]].append('+-')
            for j in range(maxbal + bal[i][0] + 1, 2 * maxbal + 1):
                ans[j].append(' ')
        else:
            for j in range(maxbal - bal[i][0]):
                ans[j].append('   ')
            ans[maxbal - bal[i][0]].append('+-')
            for j in range(maxbal - bal[i][0] + 1, maxbal + bal[i][0]):
                ans[j].append('|')
            ans[maxbal + bal[i][0]].append('+-')
            for j in range(maxbal + bal[i][0] + 1, 2 * maxbal + 1):
                ans[j].append('   ')
    else:
        if bal[i - 1][1] == 1:
            for j in range(2 * maxbal + 1):
                ans[j].append(' ')
            for j in range(maxbal - stack[-1]):
                ans[j].append(' ')
            ans[maxbal - stack[-1]].append('-+')
            for j in range(maxbal - stack[-1] + 1, maxbal + stack[-1]):
                ans[j].append('  |')
            ans[maxbal + stack[-1]].append('-+')
            for j in range(maxbal + stack[-1] + 1, 2 * maxbal + 1):
                ans[j].append(' ')
        else:
            for j in range(maxbal - stack[-1]):
                ans[j].append(' ')
            ans[maxbal - stack[-1]].append('-+')
            for j in range(maxbal - stack[-1] + 1, maxbal + stack[-1]):
                ans[j].append('|')
            ans[maxbal + stack[-1]].append('-+')
            for j in range(maxbal + stack[-1] + 1, 2 * maxbal + 1):
                ans[j].append(' ')
        stack.pop()
for i in ans:
    print(''.join(i))
