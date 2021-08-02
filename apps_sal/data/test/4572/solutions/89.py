import string
S = set(input())
for i in range(97, 123):
    s = chr(i)
    if s not in S:
        print(s)
        break
else:
    print(None)
