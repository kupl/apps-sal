'''Author- Akshit Monga'''
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    m = min(arr)
    ans = 0
    for i in arr:
        ans += (k - i) // m
    print(ans - (k - m) // m)
