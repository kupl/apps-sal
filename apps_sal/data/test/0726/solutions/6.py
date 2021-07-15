def main():
    #string     input()
    #strList    input().split()
    #integer    int(input())
    n, d = list(map(int, input().split()))
    x = list(map(int, input().split()))
    ret = 2
    for i in range(n - 1):
        if x[i + 1] - x[i] >= 2 * d:
            ret += 1 + (x[i + 1] - x[i] >= 2 * d + 1)
    print(ret)
    return 0
main()

