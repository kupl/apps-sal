def find(n, k):
    if k % 3 != 0:
        if n % 3 == 0:
            return "Bob"
        else:
            return "Alice"
    position = n % (k + 1)
    if position == k:
        return "Alice"
    if position % 3 == 0:
        return "Bob"
    else:
        return "Alice"


ans = []
for _ in range(int(input())):
    n, k = list(map(int, input().strip().split(' ')))
    ans += [find(n, k)]
print("\n".join(ans))
