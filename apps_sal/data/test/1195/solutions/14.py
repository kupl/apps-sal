n = int(input())
s = input().split()
a = int(s[0])
for i in range(n):
    a = min(a, int(s[i]))
print(2 + (a^int(s[2])))

