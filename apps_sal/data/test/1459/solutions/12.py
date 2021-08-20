a = int(input())
s = list(map(int, input().split()))
(c, d) = list(map(int, input().split()))
if c > d:
    (c, d) = (d, c)
total = 0
sum = 0
for i in range(len(s)):
    total = total + s[i]
for i in range(c - 1, d - 1):
    sum = sum + s[i]
print(min(sum, total - sum))
