n = int(input())
letters = list(map(int, input().split(' ')))
for i in reversed(list(range(n))):
    if all(x == 0 for x in letters[-(i + 1):]):
        letters = letters[:-(i + 1)]
count = 0
prev = -1
for x in letters:
    if x == 1 or prev == 1:
        count += 1
    prev = x
print(count)

