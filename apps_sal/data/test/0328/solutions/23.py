a = int(input())
max = 0
for i in range(a):
    b = input().split()
    c = int(b[1])
    b = int(b[0])
    if max < b + c:
        max = b + c
print(max)
