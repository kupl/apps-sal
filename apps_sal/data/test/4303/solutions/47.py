n,k = map(int, input().split())

lis = sorted(list(map(int, input().split())))

ans = []
for i in range(n-k+1):
    a = lis[i]
    b = lis[i+k-1]
    ans.append(min(abs(a)+abs(b-a),abs(b)+abs(a-b)))

print(min(ans))
