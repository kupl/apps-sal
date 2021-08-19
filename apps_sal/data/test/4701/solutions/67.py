n = int(input())
k = int(input())
num = 1
count = 0
while count < n:
    num = min(num * 2, num + k)
    count += 1
print(num)
