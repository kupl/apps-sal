N = int(input())
S = list(input())
print(''.join((chr(65 + (ord(s) - 65 + N) % 26) for s in S)))
