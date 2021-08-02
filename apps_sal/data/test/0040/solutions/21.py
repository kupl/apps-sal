import sys

n = int(input())

kek = False
changed = False

prev = 9999
for i in range(n):
    x, y = list(map(int, input().split()))
    if x != y:
        changed = True
    if y > prev:
        kek = True
    prev = y

if not kek and not changed:
    print("maybe")
elif kek and not changed:
    print("unrated")
else:
    print("rated")
