# A - Security
# https://atcoder.jp/contests/abc131/tasks/abc131_a

s = input()

result = 'Good'
i = 0
j = 1
while j < len(s):
    if s[i] == s[j]:
        result = 'Bad'
        break

    i += 1
    j += 1

print(result)
