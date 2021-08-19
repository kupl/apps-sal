x = input()
z = [char for char in x]
new_set = set(z)
if len(new_set) % 2 == 0:
    print('CHAT WITH HER!')
if len(new_set) % 2 != 0:
    print('IGNORE HIM!')
