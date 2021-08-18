T = int(input())


def solve():
    [A, B] = list(map(int, input().split()))

    def helper(A, B):
        count = 0
        while A != B:
            if A > B:
                return False
            if 8 * A <= B:
                A *= 8
                count += 1
            elif 4 * A <= B:
                A *= 4
                count += 1
            elif 2 * A <= B:
                A *= 2
                count += 1
            else:
                return -1
        return count

    return helper(min(A, B), max(A, B))


for _ in range(T):
    print(solve())
