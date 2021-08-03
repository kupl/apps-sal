from string import ascii_lowercase as letters

s = input()
books = set()

for i in range(len(s) + 1):
    for l in letters:
        books.add(s[:i] + l + s[i:])

print(len(books))
