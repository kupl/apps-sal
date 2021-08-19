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
