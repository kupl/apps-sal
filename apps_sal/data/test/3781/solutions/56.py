def solve(n, a):
    if n % 2 == 0:
        cnt = dict()
        for x in a:
            if x not in cnt:
                cnt[x] = 0
            cnt[x] += 1
        for v in cnt.values():
            if v % 2:
                print("First")
                return
        print("Second")
        return
    print("Second")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [*map(int, input().split())]
        solve(n, a)


main()
