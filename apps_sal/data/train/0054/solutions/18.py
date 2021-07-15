t = int(input())
for _ in range(t):
    input()
    s = [int(x) for x in input().split()]
    mysum = sum([x for x in s if x <= 2048])
    print("YES" if mysum >= 2048 else "NO")


