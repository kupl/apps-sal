import sys
n = int(input())
s = input()
state = [0] * 10
for c in s:
    if c == 'L':
        i = 0
        while state[i] == 1:
            i += 1
        state[i] = 1
    elif c == 'R':
        i = 9
        while state[i] == 1:
            i -= 1
        state[i] = 1
    else:
        i = int(c)
        state[i] = 0
print(''.join(map(str, state)))
