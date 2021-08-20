s = input()
n = len(s)
move = 0
if s[0] == s[-1]:
    move = 1
move = (n - move) % 2
if move == 1:
    print('First')
else:
    print('Second')
