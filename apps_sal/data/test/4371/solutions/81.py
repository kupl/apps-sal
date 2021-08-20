s = input()
l = len(s)
T = 753
ans = float('INF')
for i in range(l - 2):
    num_str = s[i] + s[i + 1] + s[i + 2]
    num = int(num_str)
    ans = min(ans, abs(T - num))
print(ans)
