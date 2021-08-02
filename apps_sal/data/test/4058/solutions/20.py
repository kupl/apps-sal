n, r = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

l = 0
i = 1
end = 0
while i <= n:
    j = i + r - 1
    j = min(j, n)
    while j >= end and j <= n and a[j] < 1:
        j -= 1
    if j > end:
        l += 1
        end = j
        i = j + r
    else:
        l = -1
        break

print(l)
