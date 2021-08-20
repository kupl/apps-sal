n = int(input())
k = int(input())
num = 1
for i in range(n):
    if num * 2 <= num + k:
        num *= 2
    else:
        num += k
print(num)
