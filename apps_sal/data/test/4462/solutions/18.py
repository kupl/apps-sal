N = int(input())
A = list(map(int, input().split()))
x = 0
y = 0

for a in A:
    if a % 4 == 0:
        x += 1
    elif a % 2 == 0:
        y += 1

if N // 2 <= x + y // 2:
    print("Yes")
else:
    print("No")
