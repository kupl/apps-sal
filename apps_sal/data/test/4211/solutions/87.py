N = int(input())
B = tuple(map(int, input().split()))

result = 0
tmp = 0
for i in B:
    result += min(tmp, i)
    tmp = i

result += B[0] + B[-1]

print(result)
