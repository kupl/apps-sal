(n, t) = map(int, input().split())
t_list = list(map(int, input().split()))
s = 0
for i in range(1, n):
    if t_list[i] - t_list[i - 1] >= t:
        s += t
    else:
        s += t_list[i] - t_list[i - 1]
print(s + t)
