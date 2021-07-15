n = int(input())
s = input()
a = s.count('0')
b = n - a
if a == b:
    res = [s[0], s[1:]]
else:
    res = [s]
print(len(res))
print(*res)
