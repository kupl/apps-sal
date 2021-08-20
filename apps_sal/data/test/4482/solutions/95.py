N = int(input())
a = list(map(int, input().split()))
ave = sum(a) / N
if ave >= 0 and ave % 1 >= 0.5:
    ave = int(ave) + 1
elif ave < 0 and -ave % 1 >= 0.5:
    ave = int(ave) - 1
else:
    ave = int(ave)
ans = 0
for i in a:
    ans += (i - ave) ** 2
print(ans)
