from sys import stdin
pos = input()
col = pos[0]
lig = int(pos[1])
if (col == 'a' or col == 'h') and (lig == 1 or lig == 8):
    print(3)
elif col == 'a' or col == 'h' or lig == 1 or (lig == 8):
    print(5)
else:
    print(8)
