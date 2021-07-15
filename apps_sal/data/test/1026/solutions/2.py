n = int(input())
A = list(map(int, input().split()))
B = [A[i] - (i + 1) for i in range(n)]
aaa = {}
i = 0
for key in B:
    aaa[key] = aaa.get(key, 0) + A[i]
    i += 1
print(max(aaa.values()))
