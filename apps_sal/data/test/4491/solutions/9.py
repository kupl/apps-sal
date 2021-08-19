N = int(input())
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
maxim = 0
for i in range(N):
    count = 0
    count += sum(a1[:i + 1]) + sum(a2[i:])
    if count > maxim:
        maxim = count
print(maxim)
