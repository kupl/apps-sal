n = int(input())
al = list(map(int, input().split()))

ans = [0]*(10**5+2)

for a in al:
    ans[a] += 1
    ans[a-1] += 1
    ans[a+1] += 1

print(max(ans))
