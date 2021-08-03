n = int(input())
s = input()
a = "abcdefghijklmnopqrstuvwxyz".upper() * 2

for i in s:
    b = a[a.index(i) + n]
    print(b, end="")
