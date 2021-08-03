def resolve():
    n = int(input())
    ans = 'No'
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == n:
                ans = 'Yes'
    print(ans)


resolve()
