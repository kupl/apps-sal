from collections import Counter

n = int(input())

string = [input() for i in range(n)]

string.sort()

i = Counter(string)

print((len(i)))
