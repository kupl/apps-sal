N = int(input())
H = list(map(int, input().split()))
count = N
for i in range(N - 1):
    j = -1 - i
    if H[j] < max(H[:j]):
        count -= 1
print(count)
