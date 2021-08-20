n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in range(n):
    ans.append(sum(a[0:i + 1]) + sum(b[i:n]))
print(max(ans))
