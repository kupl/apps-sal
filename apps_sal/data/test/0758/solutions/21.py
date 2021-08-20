input()
print(int(''.join(('0' if c == 'R' else '1' for c in input()[::-1])), 2))
