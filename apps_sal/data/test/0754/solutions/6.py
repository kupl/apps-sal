n = int(input())
s = input()
k = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        k += 1
print(k)
