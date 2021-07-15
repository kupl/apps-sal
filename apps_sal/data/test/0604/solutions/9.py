n = input()
a = list(map(int, input().split()))

b = set(a)
b.add(0)
b.remove(0)

print(len(b))
