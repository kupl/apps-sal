t = int(input())
for _ in range(t):
    (A, B) = list(map(int, input().split()))
    ans = 0
    nines = 9
    while nines <= B:
        ans += A
        nines = nines * 10 + 9
    print(ans)
