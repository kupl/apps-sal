def solve():
    n, m = list(map(int, input().split()))
    A, B = set(), set()
    for i in range(n):
        A.add(input().rstrip())
    for i in range(m):
        B.add(input().rstrip())
    C = A & B
    return len(A) + len(C)%2 > len(B)

print('YES' if solve() else 'NO')

