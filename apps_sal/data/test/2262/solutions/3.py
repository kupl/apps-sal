input()
a = input().split()
x = set()
for i in a:
    x.add(str(set(sorted(list(i)))))
print(len(x))
