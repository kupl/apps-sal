s = input()
pos = 1
answer = 0
while pos < len(s):
    if s[pos] == '1':
        answer += 10
        pos += 2
    else:
        answer += ord(s[pos]) - ord('0')
        pos += 1
print(1 + answer)
