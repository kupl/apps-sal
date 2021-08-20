import sys
if False:
    inp = open('C.txt', 'r')
else:
    inp = sys.stdin


def inverse(string):
    ans = ''
    for char in string:
        if char == '*':
            ans += '+'
        else:
            ans += '*'
    return ans


def recursion(k):
    if k == 0:
        return ['+']
    ans = recursion(k - 1)
    ans = ans + ans
    for i in range(2 ** (k - 1)):
        ans[i] = 2 * ans[i]
        ans[i + 2 ** (k - 1)] += inverse(ans[i + 2 ** (k - 1)])
    return ans


k = int(inp.readline())
for string in recursion(k):
    print(string)
