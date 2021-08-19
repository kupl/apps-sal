(n, t, c) = tuple(map(int, input().split()))
s = list(map(int, input().split()))
k = 0
i = 0
j = 0
while i < n:
    if s[i] > t:
        j = 0
    else:
        j += 1
        if j >= c:
            k += 1
    i += 1
print(k)
