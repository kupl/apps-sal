n = int(input())
L = list(map(int, input().split()))
Taken = [False] * n
for item in L:
    Taken[item - 1] = True
for i in range(n):
    if not Taken[i]:
        print(i + 1)
        break
