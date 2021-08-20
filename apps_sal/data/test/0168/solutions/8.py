n = int(input())
s = input()
t = 0
for i in s:
    if i == '+':
        t += 1
    else:
        t = max(t - 1, 0)
print(max(t, 0))
