n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split())) + [0]
ans, tmp_b = 0, 0

for i in range(n+1):
    ans += min(al[i], tmp_b+bl[i])
    tmp_b = max(0, bl[i] - max(0, al[i]-tmp_b))
    # print(ans, tmp_b)

print(ans)


