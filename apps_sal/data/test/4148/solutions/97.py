N = int(input())
S = input()
T = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for c in S:
    print(T[(T.index(c) + N) % 26], end='')
print()
