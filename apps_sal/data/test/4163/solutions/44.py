n = int(input())
count = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == b:
        count += 1
        if count == 3:
            print("Yes")
            return
    else:
        count = 0

print("No")
