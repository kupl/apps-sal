(n, k) = map(int, input().split())
A = list(map(int, input().split()))
index = A.index(1)
ans = index // (k - 1) + (n - index - 1) // (k - 1)
right = index % (k - 1)
left = (n - index - 1) % (k - 1)
if right:
    if left:
        if right + left <= k - 1:
            ans += 1
        else:
            ans += 2
    else:
        ans += 1
elif left:
    ans += 1
print(ans)
