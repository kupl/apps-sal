n = int(input())
A = list(map(int, input().split()))
ans = [0] * 201
for a in A:
    for i in range(-100, 101):
        ans[i + 100] += (a - i)**2
print(min(ans))
