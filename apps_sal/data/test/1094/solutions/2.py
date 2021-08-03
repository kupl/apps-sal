n = int(input())
strings = []
s = set()
for i in range(n):
    strings.append(input())

for f in strings[::-1]:
    if f not in s:
        s.add(f)
        print(f)
