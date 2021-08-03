for _ in range(int(input())):
    n = int(input())
    count = 0
    ans = ["" for i in range(n)]
    for i in range(n):
        if count >= 3 * n:
            ans[i] = "8"
        elif 3 * n - count >= 4:
            ans[i] = "9"
            count += 4
        else:
            ans[i] = "8"
            count += 4
    print("".join(ans))
