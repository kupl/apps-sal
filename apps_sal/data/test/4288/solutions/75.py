[a, b, c] = list(map(int, input().split()))
ans = 'Yes'
if a == b and a == c:
    ans = 'No'
elif a != b and a != c and (b != c):
    ans = 'No'
print(ans)
