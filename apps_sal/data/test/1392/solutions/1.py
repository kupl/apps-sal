def valid(x, k):
    for item in L:
        if(item not in x):
            return False
    return True


n, k = list(map(int, input().split()))
ans = 0
L = []
for i in range(k + 1):
    L.append(str(i))
for i in range(n):
    x = input()
    if(valid(x, k)):
        ans += 1
print(ans)
