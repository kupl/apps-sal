n = int(input())
s = input()

index = 0
while index < n:
    if s[index:index + 3] == 'fox':
        s = s[0:index] + s[index + 3:len(s)]
        index -= 2
    else:
        index += 1

print(len(s))
