N = int(input())
S = input()
ans = ''
for letter in S:
    ans += chr((ord(letter) + N - ord('A')) % 26 + ord('A'))
print(ans)
