b = int(input())
lst = list(map(int, input().split()))

# 例１
lst[0] -= 1
for i in range(1, b):
    if lst[i - 1] < lst[i]:
        lst[i] -= 1
for i in range(1, b):
    if lst[i] < lst[i - 1]:
        print("No")
        break
else:
    print("Yes")
