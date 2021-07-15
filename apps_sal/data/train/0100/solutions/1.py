t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))
    li = sorted(li)
    if li[0] + li[1] <= li[2]:
        print(li[0] + li[1])
    else:
        print(sum(li) // 2)
