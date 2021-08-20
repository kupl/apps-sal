n = int(input())
a = list(map(int, input().split()))
tmp_max = max(a)
tmp_min = min(a)
ans = tmp_max - tmp_min
print(ans)
