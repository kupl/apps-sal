from collections import Counter

l = int(input())
s = input()

c = Counter(s)

if c["1"] == 0:
    print("0")
else:
    print("1" + c["0"] * "0")
