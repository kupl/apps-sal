c = input()
letters = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    if c == letters[i]:
        print(letters[i + 1])
