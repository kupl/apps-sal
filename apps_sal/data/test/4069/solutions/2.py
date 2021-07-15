x, k, d = map(int, input().split())
cur = abs(x)
rem = k
cnt = min(cur // d, k)
cur -= d * cnt
rem -= cnt
if rem > 0:
    if rem % 2 == 1:
        cur = cur - d

ans = abs(cur) 
print(ans)
