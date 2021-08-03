direction = input()
text = input()

if direction == 'R':
    _to = 'qwertyuioasdfghjklzxcvbnm,.'
    _from = 'wertyuiopsdfghjkl;xcvbnm,./'

if direction == 'L':
    _to = 'wertyuiopsdfghjkl;xcvbnm,./'
    _from = 'qwertyuioasdfghjklzxcvbnm,.'

table = text.maketrans(_from, _to)
print(text.translate(table))
