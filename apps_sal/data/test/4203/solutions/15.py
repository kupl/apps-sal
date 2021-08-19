s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1 and (sum([int(c.islower()) for c in s]) == len(s) - 2):
    print('AC')
else:
    print('WA')
