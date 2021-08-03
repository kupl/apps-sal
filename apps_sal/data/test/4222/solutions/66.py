n, k = map(int, input().split())
s = set(range(1, -~n))
for _ in range(k):
    input()
    s -= set(map(int, input().split()))
print(len(s))
