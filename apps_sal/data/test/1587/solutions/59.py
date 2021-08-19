n = int(input())
cl = input()
if cl[:cl.count('R')].count('W') != 0:
    print(min(cl[:cl.count('R')].count('W'), cl.count('R')))
else:
    print(0)
