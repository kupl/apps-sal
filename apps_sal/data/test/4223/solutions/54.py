n = int(input())
s = input()


for x in range(1, n):
    if s[x] == s[x - 1]:
        n -= 1

print(n)
