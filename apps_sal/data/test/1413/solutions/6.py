r = 0
n = int(input())
s = input()
for i in range(n):
    if int(s[i]) % 2 == 0:
        r += i + 1

print(r)
