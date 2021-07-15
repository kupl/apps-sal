from collections import Counter

n = int(input())
c = Counter(input())

flag = False
for char in c:
    if c[char] >= 2: flag = True

if n==1 or flag:
    print("Yes")
else:
    print("No")
