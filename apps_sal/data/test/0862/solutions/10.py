n = int(input())
s = input().split(' ')
for i in range(n):
    s[i] = int(s[i])
round = 1000000000
for i in range(n):
    if round > s[i] // n:
        round = s[i] // n
for i in range(n):
    s[i] -= round * n
i = 0
time = 0
while 1:
    if s[i] <= time:
        break
    i = (i + 1) % n
    time += 1
print(i + 1)
