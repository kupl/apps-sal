N = int(input())
A_lis = list(map(int, input().split()))
a = 0
for i in A_lis:
    a += 1 / i
ans = 1 / a
print(ans)
