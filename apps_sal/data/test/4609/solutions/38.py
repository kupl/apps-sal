n = int(input())
a = [int(input()) for _ in range(n)]
s = set()
for x in a:
    if x in s:
        s.remove(x)
    else:
        s.add(x)
print(len(s))
