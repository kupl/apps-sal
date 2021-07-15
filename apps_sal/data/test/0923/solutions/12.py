n = int(input())
#x, y = map(int, input().split(" "))
arr = input().split(" ")
for i in range(n):
    arr[i] = int(arr[i])

rotate = ( n - arr[0] ) % n
for i in range(1, n):
    if i%2 == 0:
        if (arr[i]+rotate) % n != i:
            print("No")
            quit()
    else: 
        if (arr[i]-rotate) % n != i:
            print("No")
            quit()

print("Yes")
