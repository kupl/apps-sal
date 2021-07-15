n = int(input())
lst = list(input())
count = 0

if n % 2 == 0:
    for i in range(n // 2):
        if lst[i] == lst[i + n // 2]:
            count += 1

if count == n / 2:
    print("Yes")
else:
    print("No")
