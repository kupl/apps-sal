n = int(input())
B = list(map(int, input().split()))
tmp = B[0]
ans = 0
B.append(B[-1])
for b in B:
    ans += min(tmp, b)
    tmp = b
print(ans)
