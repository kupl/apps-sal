n = int(input())
A = list(map(int, input().split()))
ans = [0] * n
for a in A:
    ans[a - 1] += 1
for i in ans:
    print(i)
