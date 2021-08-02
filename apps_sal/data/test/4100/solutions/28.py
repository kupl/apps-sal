n, k, q = map(int, input().split())
correct = [0] * n

for i in range(q):
    a = int(input())
    correct[a - 1] += 1

for i in range(n):
    if k - q + correct[i] > 0:
        print('Yes')
    else:
        print('No')
