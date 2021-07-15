n = int(input())
A = list(map(int, input().split()))
A.sort()
x = A[-1]
used = [0] * (x + 1)
y = 0
for i in A:
    if x % i == 0:
        if used[i] == 1:
            y = max(y, i)
        else:
            used[i] = 1
    else:
        y = max(y, i)
print(x, y)
