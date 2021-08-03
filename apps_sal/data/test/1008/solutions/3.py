s = input()
k = int(input())


def solve(s, k):
    if len(s) % k > 0:
        print("NO")
        return
    l = len(s) // k
    for i in range(k):
        for j in range(l // 2):
            if s[i * l + j] != s[i * l + l - j - 1]:
                print("NO")
                return
    print("YES")


solve(s, k)
