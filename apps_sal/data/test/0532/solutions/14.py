NUM_OF_ALPHABET = ord('z') - ord('a') + 1
s = input()
total = 0
cur = 'a'
for c in s:
    total += min((ord(cur) - ord(c) + NUM_OF_ALPHABET) % NUM_OF_ALPHABET, (ord(c) - ord(cur) + NUM_OF_ALPHABET) % NUM_OF_ALPHABET)
    cur = c
print(total)
