n = int(input())
s = input()
alth = "abcdefghijklmnopqrstuvwxyz"
ans = n - 1
for i in range(1, n):
    if alth.find(s[i]) < alth.find(s[i - 1]):
        ans = i - 1
        break

for i in range(n):
    if i != ans:
        print(s[i], end="")
