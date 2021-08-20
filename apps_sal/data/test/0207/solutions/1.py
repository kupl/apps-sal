n = int(input())
arr = list(map(int, input().split()))
if n % 2 == 0:
    print('No')
elif arr[0] % 2 == 1 and arr[-1] % 2 == 1:
    print('Yes')
else:
    print('No')
