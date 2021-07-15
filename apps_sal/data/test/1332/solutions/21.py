a = list(map(int, input().split()))
if sum(a) > 0 and sum(a) % 5 == 0:
    print(sum(a) // 5)
else:
    print(-1)
