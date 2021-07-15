from collections import Counter

string = Counter(input())

for _ in string.values():
    if _ > 1:
        print("no")
        break
else:
    print("yes")
