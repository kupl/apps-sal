n = int(input())
s = input()
c = 0

for i in range(1, 1 + len(s) // 2):
    if s[:i] == s[i:2 * i]:
        c = i

if c != 0:
    print(n - c + 1)

else:
    print(n)

