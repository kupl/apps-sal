n = int(input())
x = sorted(list(map(int, input().split())))
ans = 1
for i in range(n):
    if(x[i] < i // ans):
        ans += 1
print(ans)
