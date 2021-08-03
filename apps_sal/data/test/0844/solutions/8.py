'''input
8
00001111
'''

n = int(input())
s = input()

bal = n
firstseen = [-1] * ((n * 2) + 1)
firstseen[n] = 0

ans = 0
for i in range(1, n + 1):
    if s[i - 1] == '1':
        bal += 1
    else:
        bal -= 1

    if firstseen[bal] != -1:
        ans = max(ans, i - firstseen[bal])
    else:
        firstseen[bal] = i

print(ans)
