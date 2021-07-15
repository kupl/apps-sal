from sys import stdin
input = stdin.readline
a = input()
s = input().rstrip("\n")
a = s.count("1")
b = s.count("0")
print(abs(a-b))

