N = int(input())
ans = (N % 1000)
if ans != 0:
    ans = 1000 - ans
print(ans)
