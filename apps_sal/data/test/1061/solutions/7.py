for ri in range(5):
    row = input().split(' ')
    if '1' in row:
        print(abs(2 - ri) + abs(2 - row.index('1')))
