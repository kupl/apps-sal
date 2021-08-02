n = int(input())
num = list(map(int, input().split()))

for i in range(1, n - 1):
    if num[i - 1] < num[i]:
        num[i] -= 1
    if num[i] > num[i + 1]:
        print("No")
        break
else:
    print("Yes")
