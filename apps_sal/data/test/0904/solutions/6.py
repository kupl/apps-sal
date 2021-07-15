_ = input()
s = input().split(' ')

max_count = 0

for word in s:
    count = 0
    for letter in word:
        if 'A' <= letter <= 'Z':
            count += 1

    max_count = max(count, max_count)

print(max_count)
