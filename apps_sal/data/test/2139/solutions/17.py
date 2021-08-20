string = input()
result = 0
pos = string.find('bear')
while pos >= 0:
    result += len(string) - (pos + 3)
    string = string[1:]
    pos = string.find('bear')
print(result)
