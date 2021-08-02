alphabet = [chr(i) for i in range(97, 123)]
S = set(list(input()))
for s in S:
    if s in alphabet: alphabet.remove(s)

print(alphabet[0]) if alphabet else print("None")
