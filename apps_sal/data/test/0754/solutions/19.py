n = int(input())
t = input()
s, i = 0, 0
while i < n:
    x = t[i]
    i += 1
    while i < n and t[i] == x:
        i += 1
        s += 1
print(s)

