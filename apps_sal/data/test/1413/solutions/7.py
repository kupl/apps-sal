n = int(input())
s = input()
k = 0
for i in range(1, n + 1):
    d = int(s[i - 1])
    if d % 2 == 0:
        k += i
print(k)
