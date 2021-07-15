n = int(input())
for i in range(n):
    L, v, l, r = list(map(int, input().split()))
    count = L // v - (r // v - (l - 1) // v)
    print(count)

