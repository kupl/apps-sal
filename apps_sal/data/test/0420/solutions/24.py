(n, m) = map(int, input().split())
mat = [input() for _ in range(n)]
ans = n
while ans > 1 and ans % 2 == 0:
    if mat[:ans] == list(reversed(mat[:ans])):
        ans //= 2
    else:
        break
    if ans == 1:
        if len(set(mat)) > 1:
            ans = 2
        break
print(ans)
