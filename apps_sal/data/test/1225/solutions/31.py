H = int(input())
num = 1
sum = 0
while H != 0:
    H = H//2
    sum += num
    num *= 2
print(sum)
