N = int(input())
a = list(map(int, input().split()))
num = [0] * N
for i in range(N):
    num[a[i] - 1] = i
for i in num:
    print(i + 1, end=' ')
