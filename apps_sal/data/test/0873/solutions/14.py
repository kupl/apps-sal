n = int(input())
a1 = input().strip()
a2 = input().strip()
res = 0
for i in range(n):
    symbA1 = int(a1[i])
    symbA2 = int(a2[i])
    res += min(abs(symbA2 - symbA1), abs(min(symbA2, symbA1) + 10 - max(symbA1, symbA2)))
print(res)
