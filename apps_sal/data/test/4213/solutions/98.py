n = int(input())
num = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i, n):
        num1 = abs(num[i] - num[j])
        if ans <= num1:
            ans = num1
print(ans)
