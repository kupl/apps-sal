n = int(input())
s = input()
d = []
for i in s:
    d.append(i)
    if len(d) >= 2:
        if d[-1] == '0' and d[-2] == '1' or (d[-1] == '1' and d[-2] == '0'):
            d.pop()
            d.pop()
print(len(d))
