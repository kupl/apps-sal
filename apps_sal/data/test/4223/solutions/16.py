n = int(input())
s = input()
x = n
for i in range(n-1):
    if s[i] == s[i+1]:
        x -= 1
print(x)
