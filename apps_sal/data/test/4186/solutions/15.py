n = int(input())
a = sorted(list(map(int, input().split())))
answer = 0
for q in range(0, n, 2):
    answer += a[q+1]-a[q]
print(answer)

