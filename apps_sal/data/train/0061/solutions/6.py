def main():
    # n ,m= map(int,input().split())
    # arr = list(map(int,input().split()))
    # b = list(map(int,input().split()))
    # n = int(input())
    # string = str(input())
    # a = list(map(int,input().split()))
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 2):
        if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
            print("YES")
            print(i + 1, i + 2, i + 3)
            return
    print("NO")


# main()
def test():
    t = int(input())
    while t:
        main()
        t -= 1


test()
