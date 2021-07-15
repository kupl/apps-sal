n = int(input())

for _ in range(n):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    print(sum(arr[:k+1]))

