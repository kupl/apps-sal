s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    if i in s:
        alphabet = alphabet.replace(i,"")

if len(alphabet) == 0:
    print("None")
else:
    print(alphabet[0])
