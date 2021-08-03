n = int(input())
size = int(input())
k = []
for m in range(n):
    k.append(int(input()))
k.sort()
num = 0
while size > 0:
    size = size - k.pop()
    num = num + 1
print(num)
