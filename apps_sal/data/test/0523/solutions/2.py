from collections import defaultdict
n, m = list(map(int, input().split()))
dict = defaultdict(int)
larr = ''
rarr = ''
mxeq = ''
mxln = 0
for _ in range(n):
    s = input()
    if dict[s[::-1]] == 1:
        rarr += s
        larr = s[::-1] + larr
        del dict[s[::-1]]
    elif s == s[::-1]:
        if len(s) > mxln:
            mxln = len(s)
            mxeq = s
    else:
        dict[s] = 1

farr = larr + mxeq + rarr
print(len(farr))
print(farr)
