import sys
input = sys.stdin.readline
s = str(input().strip())
n = len(s)
if s[0] is s[n - 1]:
    move = 1
else:
    move = 0
move = (n - move) % 2
if move is 1:
    print('First')
else:
    print('Second')
