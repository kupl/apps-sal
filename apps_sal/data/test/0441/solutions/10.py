n, a, b = map(int, input().split())
s = input()

last = ''
total = 0

for c in s:
    if c == '.':
        if not last in ['a', 'b']:
            if a >= b and a > 0:
                last = 'a'
                total += 1
                a -= 1
            elif b >= a and b > 0:
                last = 'b'
                total += 1
                b -= 1
            else:
                last = c
        elif last == 'a':
            if b > 0:
                last = 'b'
                total += 1
                b -= 1
            else:
                last = '.'
        else:
            if a > 0:
                last = 'a'
                total += 1
                a -= 1
            else:
                last = '.'
    else:
        last = c

print(total)
