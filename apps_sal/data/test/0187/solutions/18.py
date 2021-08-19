n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
if len(set(arr)) != 2 or n % 2 == 1:
    print('NO')
else:
    (a, b) = map(int, list(set(arr)))
    if arr.count(a) == arr.count(b):
        print('YES')
        print(a, b)
    else:
        print('NO')
