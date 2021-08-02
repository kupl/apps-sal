l = int(input())
s = [char for char in input()]
cc = 0

other_char = {'a': 'b', 'b': 'a'}

for i in range(0, l, 2):
    if s[i] == s[i + 1]:
        cc += 1
        s[i] = other_char[s[i]]

print(cc)
print(''.join(s))
