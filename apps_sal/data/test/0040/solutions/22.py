import sys
n = int(input())

kek = []

for i in range(n):
    a, b = (int(i) for i in input().split())
    kek.append(a)
    if a != b:
        print("rated")
        return

if kek == list(sorted(kek, reverse=True)):
    print("maybe")
else:
    print("unrated")
