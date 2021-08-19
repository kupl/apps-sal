(A, B, K) = map(int, input().split())
lists = []
for i in range(1, 100 + 1):
    if A % i == 0 and B % i == 0:
        lists.append(i)
print(lists[-K])
