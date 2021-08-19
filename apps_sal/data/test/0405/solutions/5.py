n = int(input())
s = input()
result = 0
for ch in s:
    if ch == '<':
        result += 1
    else:
        break
for ch in s[::-1]:
    if ch == '>':
        result += 1
    else:
        break
print(result)
