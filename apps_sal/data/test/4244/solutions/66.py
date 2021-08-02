n = int(input())
x = list(map(int, input().split()))
num = 0
for i in x:
    num += i
num = round(float(num / n))
ans = 0
for i in x:
    ans += (i - num)**2
print(ans)
