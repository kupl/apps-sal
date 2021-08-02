n = int(input())
for x in range(n + 1):
    for y in range(n + 1):
        if x * 4 + y * 7 == n:
            print("Yes")
            return
print("No")
