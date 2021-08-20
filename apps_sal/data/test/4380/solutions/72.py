(A, B) = map(int, input().split())
ans = 'No'
for C in range(1, 4):
    if A * B * C % 2 != 0:
        ans = 'Yes'
        break
print(ans)
