N = int(input())
lst = []
for i in range(N):
    P = int(input())
    lst.append(P)
ans = sum(lst) - int(max(lst) / 2)
print(ans)
