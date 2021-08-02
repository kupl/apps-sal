s = "abcdefghijklmnopqrstuvwxyz"
for i in range(int(input())):
    n, k = [int(x) for x in input().split()]

    use = s[:k]
    ln = len(use)
    ans = use * (n // ln) + use[:n % ln]
    print(ans)
