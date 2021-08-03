def solve(n):
    s = input()
    ans = 0
    flag = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            if flag == 1:
                ans += 1
                flag = 0
            else:
                flag = 1
    if flag:
        ans += 1
    return ans


for _ in range(int(input())):
    print(solve(int(input())))
