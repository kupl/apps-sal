n = int(input())
L = sorted(list(map(int, input().split())))
ans = [0, 0]
for i in range(n//2):
    ans[0] += abs(L[i] - (2*i+1))
    ans[1] += abs(L[i] - (2*i+2))
print(min(ans))
