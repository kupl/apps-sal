n = int(input())
b = list(map(int, input().split()))
a = b[0] + b[-1]
if n > 2:
    for i in range(n-2):
        if b[i] <= b[i+1]:
            a += b[i]
        else:
            a += b[i+1]
print(a)
