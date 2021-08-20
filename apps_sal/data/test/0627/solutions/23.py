n = int(input())
s = input()
l = []
for i in range(1, n):
    if s[i] < s[i - 1]:
        x = s[:i - 1] + s[i:]
        print(x)
        break
    if i == n - 1:
        print(s[:n - 1])
        break
