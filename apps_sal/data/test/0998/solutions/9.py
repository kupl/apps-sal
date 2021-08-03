n, x = map(int, input().split())

ans = []


last = 0
for i in range(1, 2 ** n):
    if ((i ^ x) > i):
        ans.append(last ^ i)
        last = i

print(len(ans))
for i in ans:
    print(i, end=" ")
