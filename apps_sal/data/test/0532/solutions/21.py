s = input()
alphabet = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), [i for i in range(1, 27)]))
summ = 0
cur_letter = 'a'
for letter in s:
    summ += min(abs(alphabet[letter] - alphabet[cur_letter]), 26 - abs(alphabet[letter] - alphabet[cur_letter]))
    cur_letter = letter
print(summ)
