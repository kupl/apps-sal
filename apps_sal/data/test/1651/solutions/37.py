def solve():
    S, P = map(int, input().split())
    for i in range(1, int(P ** 0.5) + 1):
        if P % i == 0 and P // i + i == S:
            return True
    return False


print("Yes") if solve() else print("No")
