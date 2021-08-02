N = str(input())
ans = "Yes"
for i in range(len(N) // 2):
    if N[i] != N[len(N) - i - 1]:
        ans = "No"
        break
print(ans)
