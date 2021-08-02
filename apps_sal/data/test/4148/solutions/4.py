alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
N = int(input())
S = input()
ans = ""
for i in range(len(S)):
    x = alphabet.index(S[i])
    if x + N >= 26:
        y = x + N - 26
    else:
        y = x + N
    ans += alphabet[y]
print(ans)
