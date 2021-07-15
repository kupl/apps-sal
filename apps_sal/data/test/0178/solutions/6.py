n = int(input())
s = input()
num = (n - 11) // 2
num2 = 0
num3 = -1
for i in range(n):
    if s[i] == "8":
        num2 += 1
        if num2 == num + 1:
            num3 = i
            break
if num3 == -1 or num3 > num * 2:
    print("NO")
else:
    print("YES")

