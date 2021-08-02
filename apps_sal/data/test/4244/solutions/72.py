n = int(input())
x_list = list(map(int, input().split()))
ave = sum(x_list) / n
p = int(ave) + (1 if ave - int(ave) > 1 / 2 else 0)
ans = sum([(p - x_i)**2 for x_i in x_list])
print(ans)
