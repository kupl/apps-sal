s = input()
x = ""
y = ""
x_con = 0
y_con = 0
for i in range(len(s)):
    if i % 2 == 0:
        x += "0"
        y += "1"
    else:
        x += "1"
        y += "0"

for i in range(len(s)):
    if s[i] != x[i]:
        x_con += 1
    if s[i] != y[i]:
        y_con += 1

print(min(x_con, y_con))
