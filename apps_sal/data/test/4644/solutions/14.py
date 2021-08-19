for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) % 2 == 1:
        print('YES')
    elif all((ele % 2 == 0 for ele in arr)):
        print('NO')
    elif all((ele % 2 == 1 for ele in arr)) and len(arr) % 2 == 0:
        print('NO')
    else:
        print('YES')
