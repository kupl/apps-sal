def solve(k):
    res = 0
    for i in range((k + 1) // 2):
        res += 4 * 2 * i ** 2
    return res


strr = input()
for _ in range(int(strr)):
    k = int(input())
    print(solve(k))
