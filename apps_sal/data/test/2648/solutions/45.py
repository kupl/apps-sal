N = int(input())
K = len(set(input().split()))
print(K + K % 2 - 1)
