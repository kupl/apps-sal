n = int(input())
a = list(map(int, input().split()))
b = len(a)
result = 1
i = 0
j = 0
while True:
    if a[i] == result:
        result += 1
    i += 1
    if i >= b:
        break
if result == 1:
    print(-1)
else:
    print(b - result + 1)
