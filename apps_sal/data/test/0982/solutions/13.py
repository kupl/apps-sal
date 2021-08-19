ans = []
for _ in range(int(input())):
    (a, b) = list(map(int, input().split()))
    if a * 2 <= b:
        ans.append('NO')
    else:
        ans.append('YES')
print('\n'.join(ans))
