def main():
    n = int(input())
    ans = n * (n + 1) * (n + 2) // 6
    
    for i in range(n-1):
        x, y = list(map(int, input().split()))
        if x > y:
            y, x = x, y
        ans -= x * (n - y + 1)
    print(ans)
    
main()

