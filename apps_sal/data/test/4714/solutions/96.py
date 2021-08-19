(A, B) = map(int, input().split())
res = 0
for i in range(A, B + 1):
    if str(i) == str(i)[::-1]:
        res += 1
print(res)
