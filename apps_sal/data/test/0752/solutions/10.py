n = int(input())
a = []
b = []
ans = 0

for _ in range(n):
    s = input()
    a.append(s)

for i in range(n):
    s = input()
    if s in a:
        a.remove(s)

print(len(a))
