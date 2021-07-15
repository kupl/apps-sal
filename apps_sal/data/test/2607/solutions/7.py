'''input
3
??
1?
1?
'''
from sys import stdin
def input():
    return stdin.readline()[:-1]


for _ in range(int(input())):
    s = list(input())
    for i in range(0, len(s)):
        if s[i] == '?':
            if i > 0:
                prev = s[i-1]
            else:
                prev = 'x'
            if i < len(s) - 1:
                post = s[i+1]
            else:
                post = 'x'
            for ch in list('abc'):
                if ch != prev and ch != post:
                    s[i] = ch
                    break
    correct = True
    for i in range(0, len(s) - 1):
        if s[i+1] == s[i]:
            correct = False

    print(''.join(s)) if correct else print(-1)




