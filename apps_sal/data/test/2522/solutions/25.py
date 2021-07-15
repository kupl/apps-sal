def solve(n, a, b):
    b.reverse()
    l, r = 0, n-1
    for i in range(n):
        if a[i] == b[i]:
            if (l < i) and (a[i] != b[l]) and (a[l] != b[i]):
                b[l], b[i] = b[i], b[l]
                l += 1
            elif (i < r) and (a[i] != b[r]) and (a[r] != a[i]):
                b[r], b[i] = b[i], b[r]
                r -= 1
            else:
                return "No"
    return "\n".join([
        "Yes",
        " ".join(map(str, b))
    ])

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
