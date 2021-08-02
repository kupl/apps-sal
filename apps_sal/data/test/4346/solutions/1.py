t = int(input())
for _ in range(t):
    li, v, l, r = list(map(int, input().split()))
    print(li // v + (l - 1) // v - r // v)
