n = int(input())
H = list(map(int, input().split()))
ans = 'Yes'
m = H[0]
if n == 1:
    ans
else:
    for i in range(1, n):
        if H[i] >= m - 1:
            m = max(H[i], m)
            continue
        else:
            ans = 'No'
            break
print(ans)
