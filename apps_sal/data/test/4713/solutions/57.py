N = int(input())
S = input()

result = 0
x = 0
for i in S:
    if i == 'I':
        x += 1
    else:
        x -= 1
    result = max(result, x)

print(result)
