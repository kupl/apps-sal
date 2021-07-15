from collections import Counter

s = input()
t = input()

c1 = Counter(s).most_common()
c2 = Counter(t).most_common()

for x, y in zip(c1, c2):
    if x[1] != y[1]:
        print("No")
        break
else:
    print("Yes")
