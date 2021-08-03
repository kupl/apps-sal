N, M = map(int, input().split())
A = [input() for i in range(N)]
B = [input() for i in range(M)]
ans = "Yes"
for i in A:
    for j in B:
        if j not in i:
            ans = "No"
print(ans)
