k = int(input())
sub = k // 50 + 49
ans = [sub - k % 50] * 50
for i in range(k % 50):
    ans[i] += 51
print(50)
print(*ans)
