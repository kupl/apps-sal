n = int(input())
s = input()
a = d = 0
for i in s:
    if i == 'A':
        a += 1
    if i == 'D':
        d += 1
print('Anton' if a > d else 'Danik' if d > a else 'Friendship')
