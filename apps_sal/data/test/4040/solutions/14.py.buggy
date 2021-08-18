n, m, d = map(int, input().split())
c = list(map(int, input().split()))
sum_c = sum(c)
tmp_ans = sum_c + (m + 1) * (d - 1)
if tmp_ans < n:
    print("NO")
    return
nokori = tmp_ans - n

ans = [0] * n
j = 1
for i in range(m):
    j -= 1
    if nokori >= d - 1:
        nokori -= d - 1
    else:
        j += (d - 1 - nokori)
        nokori = 0
    for _ in range(c[i]):
        ans[i + j] = i + 1
        j += 1
print("YES")
print(*ans)
