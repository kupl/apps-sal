def main():
    t = int(input())
    for i in range(t):
        steps = 0
        n,k = list(map(int,input().split()))
        while n != 0:
            if n%k == 0:
                n = n//k
                steps += 1
            else:
                steps += n%k
                n -= n%k

        print(steps)


main()

