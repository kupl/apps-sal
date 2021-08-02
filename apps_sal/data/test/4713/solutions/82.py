n = int(input())
s = input()
count = 0
x = 0
for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    count = max(count, x)
print(count)
