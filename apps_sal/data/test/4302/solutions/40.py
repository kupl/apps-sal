a,b = list(map(int,input().split()))
ans = max(a,b)
q = max(a,b)
d = min(a,b)
ans += max(q-1,d)

print(ans)

