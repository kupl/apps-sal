t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]
    arr.sort()
    if sum(arr) == 0:
        print("NO")
    elif sum(arr) > 0:
        print("YES")
        print(*arr[::-1])
    else:
        print("YES")
        print(*arr)
