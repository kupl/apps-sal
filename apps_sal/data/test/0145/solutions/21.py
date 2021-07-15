a = input().strip()
alph = [0] * 26
for i in a:
    alph[ord(i) - ord('a')] = 1
if sum(alph) % 2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')
