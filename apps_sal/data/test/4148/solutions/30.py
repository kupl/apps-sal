N = int(input())
S = input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ans = ''
for word in S:
    index = alphabet.index(word)

    new_index = (index + N) % 26
    ans = ans + alphabet[new_index]

print(ans)
