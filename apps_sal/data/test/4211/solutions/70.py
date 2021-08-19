N = int(input())
l = list(map(int, input().split()))
ans = 0
last_n = 0
for i in l:
    if i >= last_n:
        ans += i
        last_n = i
    else:
        ans -= last_n
        ans += i * 2
        last_n = i
ans += l[0]
print(ans)
