N = input()
ls = [int(s) for s in input().split()]
num = [0 for s in range(1000001)]
for i in ls:
    num[i] += 1
ans = [num[i - 1] + num[i] + num[i + 1] for i in range(100000)]
print(max(ans))
