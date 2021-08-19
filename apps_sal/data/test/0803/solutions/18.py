n = int(input())
s = input()
m = s.count('X')
count = abs(n // 2 - m)
print(count)
if m < n // 2:
    print(str.replace(s, 'x', 'X', count))
else:
    print(str.replace(s, 'X', 'x', count))
