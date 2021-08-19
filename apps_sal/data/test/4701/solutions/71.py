n = int(input())
k = int(input())
num = 1
for i in range(n):
    num = min(num * 2, num + k)
print(num)
