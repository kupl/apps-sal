def nod(a, b):
    while max(a, b) % min(a, b) != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return min(a, b)


n = int(input())
arr = list(map(int, input().split()))
x = arr[0]
for i in range(1, n):
    x = nod(arr[i], x)
print(x * n)
