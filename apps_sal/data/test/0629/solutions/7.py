n = int(input())
a1 = [int(i) for i in input().split(" ")]
a2 = [int(i) for i in input().split(" ")]
b = [int(i) for i in input().split(" ")]

res = 1111111111111
for i in range(0, n):
    for j in range(i + 1, n):
        tmp = b[i] + b[j] + sum(a1[:i]) + sum(a2[i:]) + sum(a1[:j]) + sum(a2[j:])
        if (tmp < res):
            res = tmp
print(res)
