(n, m) = list(map(int, input().split()))
ls = list(map(int, input().split()))
di = [list(map(int, input().split())) for _ in range(m)]
fi = []
for (i, j) in di:
    fi.append([j, i])
for k in ls:
    fi.append([k, 1])
fi.sort(reverse=True)
ans = 0
cnt = 0
how = 0
while True:
    if how + fi[cnt][1] < n:
        how += fi[cnt][1]
        ans += fi[cnt][1] * fi[cnt][0]
    else:
        ans += (n - how) * fi[cnt][0]
        break
    cnt += 1
print(ans)
