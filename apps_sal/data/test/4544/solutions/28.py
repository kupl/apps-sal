N = int(input())
A = [int(x) for x in input().split()]

data = {}
for a in A:
    for i in range(3):  # a-1,a,a+1をカウント
        if a - 1 + i in data:
            data[a - 1 + i] += 1
        else:
            data[a - 1 + i] = 1

# カウントしたものの最大値が答え
ans = 0
for d in data.values():
    ans = max(ans, d)
print(ans)
