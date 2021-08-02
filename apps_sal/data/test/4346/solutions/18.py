t = int(input())
for i in range(t):
    L, u, l, r = list(map(int, input().split()))
    a = L // u - (r // u - (l - 1) // u + 1)
    print(a + 1)
