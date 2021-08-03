def main():
    n = int(input())
    l1 = list(map(int, input().split()))
    N = (n * (n + 1)) / 2
    sum1 = 0
    for i in range(n):
        sum1 += l1[i]
    if(sum1 == N):
        print("YES")
    else:
        print("NO")


main()
