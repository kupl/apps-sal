N = int(input())
x_list = list(map(int, input().split()))

P = round(sum(x_list) / N)
ans = 0

for i in x_list:
    ans += (i - P) ** 2

print(ans)
