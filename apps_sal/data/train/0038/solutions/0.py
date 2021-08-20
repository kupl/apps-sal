q = int(input())
for z in range(q):
    (n, k1, k2) = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    if max(arr1) > max(arr2):
        print('YES')
    else:
        print('NO')
