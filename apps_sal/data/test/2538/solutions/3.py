T = int(input())
for i in range(T):
    s, k, f = map(int, input().split())
    print(min(f + 1, max(0, (s + f - k + 1) // 2)))
