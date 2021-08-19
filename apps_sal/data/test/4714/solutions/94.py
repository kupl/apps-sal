(a, b) = map(int, input().split())
count = 0
for i in range(a, b + 1):
    if list(map(int, list(str(i)))) == list(reversed(list(map(int, list(str(i)))))):
        count += 1
print(count)
