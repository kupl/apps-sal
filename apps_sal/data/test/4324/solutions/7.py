for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    i = 0
    ans = ""
    while len(ans) < n:
        ans += chr(ord('a')+i)
        i = (i+1) % b
    print(ans)

