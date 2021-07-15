n = int(input())
s = input()
res = 0
for i in range(n):
    if int(s[i]) % 2 == 0:
        res += i + 1
print(res)
