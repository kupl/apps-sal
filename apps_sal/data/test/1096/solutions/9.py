a = list(input())
moves = 8
resticted = ['a', 'h', '1', '8']

if a[0] in resticted and a[1] in resticted:
    moves = 3;
elif a[0] in resticted or a[1] in resticted:
    moves = 5

print(moves)
