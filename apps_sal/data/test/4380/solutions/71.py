(A, B) = map(int, input().split())
ans = 'No'
for i in range(1, 4):
    if A * B * i % 2 == 1:
        ans = 'Yes'
        break
print(ans)
