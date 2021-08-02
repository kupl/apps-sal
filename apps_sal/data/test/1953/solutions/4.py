n = int(input())
A = list(map(int, input().split()))
A.sort()
time = 0
ans = 0
for i in A:
    if i >= time:
        ans += 1
        time += i
print(ans)
