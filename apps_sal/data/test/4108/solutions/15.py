import collections
s = input()
t = input()
sc = sorted(collections.Counter(s).values())
tc = sorted(collections.Counter(t).values())


for i in range(len(sc)):
    if sc[i] != tc[i]:
        print("No")
        return
print("Yes")
