N = int(input())
A = list(map(int, input().split()))

lst = []
for i in A:
    lst.append(1/i)
ans = 1 / (sum(lst))
print(ans)
