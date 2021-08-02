def resolve():
    n = int(input())
    ans = [0] * n
    a = list(map(int, input().split()))
    for i in a:
        ans[i - 1] += 1
    for i in ans:
        print(i)


resolve()
