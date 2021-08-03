n = int(input())
list = []
i = 1
while i <= n:
    list.append(input())
    i += 1
print('AC x ', list.count('AC'))
print('WA x ', list.count('WA'))
print('TLE x ', list.count('TLE'))
print('RE x ', list.count('RE'))
