import sys

def solve():
    n, m, i, j, a, b = map(int, input().split())
    i -= 1
    j -= 1
    n -= 1
    m -= 1
    if (i == 0 or i == n) and (j == 0 or j == m): return 0
    # print(i, j)
    if (i - a < 0 and i + a > n) or (j - b < 0 and j + b > m): return "Poor Inna and pony!"
    uprow = i
    downrows = n - i
    leftcol = j
    rightcol = m - j
    # print(uprow, downrows, leftcol, rightcol)
    ans = 10000000000
    if uprow % a == 0 and leftcol % b == 0 and abs(uprow//a - leftcol//b) % 2 == 0: #upperleft
        ans = min(ans, max(uprow//a,leftcol//b))
    if uprow % a == 0 and rightcol % b == 0 and abs(uprow//a - rightcol//b) % 2 == 0: #upperright
        ans = min(ans, max(uprow//a,rightcol//b))
    if downrows % a == 0 and leftcol % b == 0 and abs(downrows//a - leftcol//b) % 2 == 0: #lowerleft
        ans = min(ans, max(downrows//a ,leftcol//b))
    if downrows % a == 0 and rightcol % b == 0 and abs(downrows//a - rightcol//b) % 2 == 0: #lowerright
        ans = min(ans, max(downrows//a , rightcol//b))

    return ans if ans != 10000000000 else "Poor Inna and pony!"



if sys.hexversion == 50594544 : sys.stdin = open("test.txt")
print(solve())
