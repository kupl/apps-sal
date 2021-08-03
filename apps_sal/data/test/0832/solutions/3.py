n = int(input())

Home = []
Away = []

for i in range(n):
    a, b = input().split()
    Home.append(a)
    Away.append(b)
ans = 0
for i in range(n):
    ans += Away.count(Home[i])
    if(Away[i] == Home[i]):
        ans -= 1

print(ans)
