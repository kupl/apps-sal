n = int(input())
s = {'purple': "Power", "green": "Time", "blue":"Space", "orange":"Soul", "red":"Reality", "yellow":"Mind"}
for i in range(n):
    u = input()
    s.pop(u)
print(6-n)
for i in s:
    print(s[i])
