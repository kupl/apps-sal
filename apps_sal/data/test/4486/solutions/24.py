

N = list(input())
ans = []
for i in range(len(N)):
    if i % 2 == 0:
        ans.append(N[i])
print(("".join(ans)))

