import string
n = int(input())
s = input()

l = string.ascii_uppercase
ans = [l[(l.index(i) + n) % len(l)] for i in s]
print(''.join(ans))
