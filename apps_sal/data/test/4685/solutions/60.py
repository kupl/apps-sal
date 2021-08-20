ABC = sorted(map(int, input().split()))
K = int(input())
print(ABC[0] + ABC[1] + ABC[2] * 2 ** K)
