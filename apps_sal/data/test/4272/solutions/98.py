n = int(input())
text = input()

count = 0
for i in range(n - 2):
    target = text[i:i + 3]
    if target == 'ABC':
        count += 1

print(count)
