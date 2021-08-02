def main():
    N, Z, W = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if N == 1:
        return abs(A[-1] - W)
    return max(abs(A[-1] - W), abs(A[-1] - A[-2]))


print((main()))
