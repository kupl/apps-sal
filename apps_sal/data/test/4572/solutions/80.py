import sys
alphabet = "abcdefghijklmnopqrstuvwxyz"
s = set(sorted(input().strip()))
for i in alphabet:
    if not i in s:
        print(i)
        return
print("None")
