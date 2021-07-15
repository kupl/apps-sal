import sys
import math

def main():
    s = input()
    q = []
    for i in range(len(s)):
        if s[i] == '1':
            q.append(i)
        elif len(q) > 0:
            q.pop();

    result = []
    q = set(q)
    for i in range(len(s)):
        if i in q:
            result.append('0')
        else:
            result.append(s[i])

    print(''.join(result))

    

def __starting_point():
    main()

__starting_point()
