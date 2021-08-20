n = int(input())
plateau = input()
i = 0
while n > i and plateau[i] == '<':
    i += 1
j = n - 1
while j >= 0 and plateau[j] == '>':
    j -= 1
if i > j:
    print(n)
else:
    print(i + (n - 1 - j))
