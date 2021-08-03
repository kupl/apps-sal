def solve(num):
    s_num = str(num)
    return len(s_num)


n = int(input())
res = []
for i in range(1, int(n**.5) + 1):
    if n % i == 0:
        x = n // i
        res.append(max(solve(x), solve(i)))
print(min(res))
