from collections import defaultdict
s = input()
s = [x for x in s]
(t, u) = ([], [])
ds = defaultdict(int)
for c in s:
    ds[c] += 1
curr_letter_index = ord('a')
curr_poz_in_s = 0
while curr_letter_index <= ord('z'):
    curr_letter = chr(curr_letter_index)
    if len(t) > 0 and ord(t[-1]) <= ord(curr_letter):
        letter = t.pop()
        u.append(letter)
    elif ds[curr_letter] > 0:
        letter = s[curr_poz_in_s]
        curr_poz_in_s += 1
        t.append(letter)
        ds[letter] -= 1
    else:
        curr_letter_index += 1
t.reverse()
print(''.join(u + t))
