for _ in range(int(input())):
    n,k = [int(s) for s in input().split()]
    ans = (n//k)*k
    ans1 = n%k
    ans+= min(k//2, ans1)
    print(ans)
