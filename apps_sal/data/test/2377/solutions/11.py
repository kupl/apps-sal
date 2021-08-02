N, H = map(int, input().split())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)


def solver(N, H, A, B):
    x = max(A)
    B.sort()
    B.reverse()

    ans = 0
    for b in B:
        if b < x:
            break
        H -= b
        ans += 1
        if H <= 0:
            return ans

    return ans + -(-H // x)


print(solver(N, H, A, B))
