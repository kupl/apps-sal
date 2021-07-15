n = int(input())
s = input()
for d in range(2, n + 1):
    if n % d == 0:
        s = s[d - 1::-1] + s[d:]
print(s)

