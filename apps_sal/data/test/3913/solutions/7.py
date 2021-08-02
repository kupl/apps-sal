n = int(input())
S = input()
HaveLetters = set(list(S))
m = int(input())
words = []
CanLetters = set([chr(i) for i in range(ord("a"), ord("z") + 1)]) - HaveLetters
for _ in range(m):
    Word = input()
    for i in range(n):
        if S[i] == "*":
            if Word[i] in HaveLetters:
                break
        else:
            if Word[i] != S[i]:
                break
    else:
        words += [Word]
ans = 0
for letter in CanLetters:
    can = True
    for Word in words:
        if letter not in Word:
            can = False
            break
    if can:
        ans += 1
print(ans)
