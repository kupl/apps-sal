def mainA():
    T = int(input())
    for i in range(T):
        s, a, b, c = map(int, input().split())
        ans = s // c
        ans += ans // a * b
        print(ans)


mainA()
