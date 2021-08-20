from collections import defaultdict
n = int(input())
li = []
s = set()
for val in range(n):
    i = int(input())
    if i in s:
        s.remove(i)
    else:
        s.add(i)
print(len(s))
