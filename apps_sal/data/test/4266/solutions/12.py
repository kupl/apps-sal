(x, k) = map(int, input().split())
ans1 = [0] * (x - 1)
ans2 = [0] * (x - 1)
for i in range(1, x):
    ans1[i - 1] = k - i
    ans2[i - 1] = k + i
ans = ans1 + ans2
ans.append(k)
ans.sort()
ke = map(str, ans)
print(' '.join(ke))
