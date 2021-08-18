A, B = map(int, input().split())

count = 0
for C in range(1, 4):
    if A * B * C % 2 == 1:
        count = count + 1
if count > 0:
    print("Yes")

else:
    print("No")
