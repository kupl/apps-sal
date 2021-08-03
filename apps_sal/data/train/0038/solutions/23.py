t = int(input())
for l in range(t):
    n, k1, k2 = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    if(max(arr1) > max(arr2)):
        print("YES")
    else:
        print("NO")
