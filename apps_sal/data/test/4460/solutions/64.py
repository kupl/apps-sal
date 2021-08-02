l = list(map(int, input().split()))
for i in range(5):
    if l[i] == 0:
        ans = i + 1
        print(ans)
