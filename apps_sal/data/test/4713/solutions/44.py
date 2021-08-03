n = int(input())
s = input()
x = 0
c = 0
for i in s:
    if i == "I":
        x += 1
    else:
        x -= 1
    c = max(x, c)
print(c)
