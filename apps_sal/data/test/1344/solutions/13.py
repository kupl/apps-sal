n = int(input())
N = list(map(int, input().split()))
counter = 1
ans = 1
for i in range(1, n):
    if N[i] > N[i - 1]:
        counter += 1
    else:
        if counter > ans:
            ans = counter
        counter = 1
if counter > ans:
    ans = counter
print(ans)
