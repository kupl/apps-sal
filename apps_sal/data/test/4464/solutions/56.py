(a, b, c) = map(int, input().split())
ans = 'NO'
for num in range(1, b + 1):
    if num * a % b == c:
        ans = 'YES'
        break
    else:
        pass
print(ans)
