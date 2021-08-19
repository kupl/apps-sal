text = input().lower()
caps = int(input()) + 97
for letter in text:
    print(letter.upper(), end='') if letter < chr(caps) else print(letter, end='')
print()
