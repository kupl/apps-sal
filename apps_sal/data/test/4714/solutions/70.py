a, b = list(map(int, input().split()))
ans = 0
for i in range(a,b+1):
    key = str(i)
    #print(key)
    if key[:2] == key[4]+key[3]:
        ans += 1
print(ans)

