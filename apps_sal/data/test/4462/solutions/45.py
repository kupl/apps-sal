n = int(input())
a = list(map(int, input().split()))
four = 0
two = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1

if four >= n // 2 or n - 2 * four <= two:
    print("Yes")
else:
    print("No")
