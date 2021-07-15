n, k = map(int, input().split())
for i in range(n, k+1):
    if len(str(i)) == len(set(str(i))):
        print(i)
        return
print(-1)
