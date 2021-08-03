import collections

input()
c = collections.Counter(list(map(int, input().split())))
for x in sorted(c, reverse=True):
    if c[x] % 2 == 1:
        print("Conan")
        break
else:
    print("Agasa")
