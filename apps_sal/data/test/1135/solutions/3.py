n = int(input())
s = input()
t = ""
i = 0
if n % 2 == 1:
    t = s[0]
    i = 1
while i < n:
    t = s[i] + t + s[i + 1]
    i += 2
print(t)
