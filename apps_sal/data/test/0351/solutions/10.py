import sys


def main():
    (n, k) = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a = sorted(a)
    ans = 0
    for i in range(n):
        if k * 2 >= a[i]:
            k = max(k, a[i])
        else:
            t = a[i]
            while t > k * 2:
                if t % 2 == 1:
                    t = int(t / 2) + 1
                else:
                    t = int(t / 2)
                ans += 1
            k = a[i]
    print(ans)


main()
