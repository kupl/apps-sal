s = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphabets)):
   if not alphabets[i] in s:
      print(alphabets[i])
      return

print('None')
