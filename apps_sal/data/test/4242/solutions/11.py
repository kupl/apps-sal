a, b, k = map(int, input().split())

ans = [i for i in range(min(a, b), 0, -1) if a%i==0 and b%i==0]
print(ans[k-1])
