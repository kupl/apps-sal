print(('YES' if (input() + ''.join(reversed(input()))).replace('X', '') \
        in (input() + ''.join(reversed(input()))).replace('X', '') * 2 else 'NO'))

