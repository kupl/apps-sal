n = int(input())

s = list(input())

letters = [0] * 26
for c in s:
    letters[ord(c) - ord('a')] += 1
it = 25


def can_be_deleted(s, i):
    if i - 1 >= 0 and i + 1 < len(s):
        return ord(s[i - 1]) + 1 == ord(s[i]) or ord(s[i + 1]) + 1 == ord(s[i])
    if i == 0:
        return ord(s[i + 1]) + 1 == ord(s[i])
    if i == len(s) - 1:
        return ord(s[i - 1]) + 1 == ord(s[i])


score = 0
while it >= 0:
    if letters[it] == 0:
        it -= 1
        continue
    i = 0
    deleted = False
    while i < len(s) and len(s) > 1:
        if s[i] == chr(ord('a') + it) and can_be_deleted(s, i):
            del s[i]
            score += 1
            deleted = True
            break
        i += 1
    if not deleted:
        it -= 1
print(score)

