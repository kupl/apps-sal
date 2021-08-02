n = input()
arr = input().split(" ")

asc = 1
x = int(arr[0])
for i in range(1, int(n)):
    if int(arr[i]) > x:
        asc += 1
    else:
        asc = 1
    x = int(arr[i])
print(int(n) - asc)
