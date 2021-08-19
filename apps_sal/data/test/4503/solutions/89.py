(H, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
a = sum(A)
if a >= H:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
