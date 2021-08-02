n = int(input())
a = list(map(int, input().split()))
four = 0
two = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1

if 2 * four + 1 >= n:
    print("Yes")
elif 2 * four + two >= n:
    print("Yes")
else:
    print("No")
