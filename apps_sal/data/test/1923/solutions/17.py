n = int(input())
array = list(map(int, input().split()))
array.sort()

ans = 0
for i in range(n * 2):
    if i % 2 == 0:
        ans += array[i]

print(ans)

