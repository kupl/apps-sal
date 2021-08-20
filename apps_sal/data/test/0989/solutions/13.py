(n, k) = list(map(int, input().split()))
l1 = list(map(int, input().split()))
l1.sort()
i = 0
j = n - 1
left = 1
right = 1
while i < j and k > 0:
    x = l1[i + 1] - l1[i]
    y = l1[j] - l1[j - 1]
    if left == right:
        if k >= left * x:
            k -= left * x
            i += 1
            left += 1
        else:
            l1[i] += k // left
            break
    elif k >= right * y:
        k -= right * y
        j -= 1
        right += 1
    else:
        l1[j] -= k // right
        break
print(l1[j] - l1[i])
