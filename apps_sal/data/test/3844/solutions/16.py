from collections import Counter
n = input()
a = list(map(int, input().split()))

counter = Counter(a)
f = 1
for i in counter.values():
    if i % 2:
        print("Conan")
        f = 0
        break


if f:
    print("Agasa")
