n = int(input())
s = input()
c = 1
sol = ''
i = 0
while i < n:
    sol += s[i]
    i += c
    c += 1
print(sol)
