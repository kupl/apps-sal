n = int(input())
s = input()
x = 0
xl = [0]
for i in range(n):
    if s[i] == "I":
        x += 1
        xl.append(x)
    else:
        x -= 1
        xl.append(x)
print(max(xl))
