n = int(input())
p = list(map(int,input().split()))
ans = 0
m = 10**18

for i in p:
    if m > i:
        m = i
        ans += 1
print(ans)
