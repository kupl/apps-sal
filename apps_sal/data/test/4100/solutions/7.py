n, k, q = map(int, input().split()); n = [k - q for _ in range(n)]
for _ in range(q): n[int(input()) - 1] += 1
[print('YNeos'[i <= 0::2]) for i in n]
