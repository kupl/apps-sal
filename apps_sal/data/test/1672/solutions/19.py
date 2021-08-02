n = int(input())
polo = 'a'
gruppi = 0
for i in range(n):
    s = input()
    if s[1] != polo:
        gruppi += 1
    polo = s[1]

print(gruppi)
