def count_capitals(string):
    count = 0
    for letter in string:
        if letter.upper() == letter:
            count += 1
    return count


n = int(input())

words = [x for x in input().split()]
capitals = []

for word in words:
    capitals.append(count_capitals(word))

print(max(capitals))
