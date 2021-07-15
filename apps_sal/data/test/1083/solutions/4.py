n = int(input())
s = sum([i for i in range(n + 1)])
print(s % 2)
ans = []
q = s // 2
for i in range(n - 1, 0, -1):
    if q >= i:
        ans = [i] + ans
        q -= i
print(len(ans), *ans)
