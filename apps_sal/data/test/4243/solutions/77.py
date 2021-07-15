def resolve():
    x = int(input())
    ans = 0
    ans += x//500*1000
    ans += x%500//5*5
    print(ans)
resolve()
