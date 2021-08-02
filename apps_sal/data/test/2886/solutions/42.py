s = input()
answer = "-1 -1"

if s[-2] == s[-1]:
    answer = "{} {}".format(len(s) - 1, len(s))

for i in range(len(s) - 2):
    if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
        answer = "{} {}".format(i + 1, i + 3)
        break

print(answer)
