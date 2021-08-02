n = int(input())

s = input()

found = n - 1

for i in range(n - 1):
    if(s[i] > s[i + 1]):
        found = i
        break

s = s[:found] + s[found + 1:]

print(s)
