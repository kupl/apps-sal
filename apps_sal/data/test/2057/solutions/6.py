def main():
    n = int(input())
    times = list(map(int, input().split()))
    mntm = set()
    mntm.add(0)
    ans = 1
    for t in range(n):
        if times[t] in mntm:
            mntm.discard(times[t])
            mntm.add(t + 1)
        else:
            ans += 1
            mntm.add(t + 1)
    print(ans)


main()

