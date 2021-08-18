def solve(N):
    N = [0] + N
    k = 0
    ans = 0
    for d, d_next in zip(N[::-1], N[-2::-1]):
        d += k
        if d <= 4 or (d == 5 and d_next < 5):
            k = 0
            ans += d
        else:
            k = 1
            ans += 10 - d
    if k:
        ans += 1
    return ans


def test(N, ans):
    for i in range(N, 10000):
        rem = i - N
        if sum(map(int, str(i))) + sum(map(int, str(rem))) < ans:
            print(f"!!! N={N}, ans={ans}, trueans={i, rem}")


def main():
    N = list(map(int, input()))
    print((solve(N)))


main()
