n = int(input())
s = input() + '0'
answer = 0
current = 0
for i in range(n + 1):
    if s[i] == '1':
        current += 1
    else:
        answer = answer * 10 + current
        current = 0
print(answer)
