from collections import Counter
def main():
    S = input()
    A = [0] * ((n := len(S)) + 1)
    A[1] = (a := int(S[-1])) % 2019
    for i in range(2, n + 1):
        a += pow(10, i - 1, 2019) * int(S[-i])
        A[i] = a % 2019
    c = Counter(A)
    ans = 0
    for v in list(c.values()):
        ans += v * (v - 1) // 2
    print(ans)

def __starting_point():
    main()

__starting_point()
