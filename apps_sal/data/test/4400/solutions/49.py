n = input()
count = 0
if 'R' in n:
    if n[0] == n[1] or n[1] == n[2]:
        count = n.count('R')
    else:
        count += 1
print(count)
