n = int(input())
lvl = input()

for start in range(0, 107):
    for jump in range(1, 40):
        if start + jump + jump + jump + jump >= len(lvl):
            break
        if lvl[start] == lvl[start + jump] == lvl[start + jump + jump] == lvl[start + jump + jump + jump] == lvl[start + jump + jump + jump + jump] == '*':
            print('yes')
            return

print('no')
