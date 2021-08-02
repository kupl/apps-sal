N = int(input())
A = list(map(int, input().split()))

gyakusuu = 0
for i in A:
    gyakusuu += 1 / i

ans = 1 / gyakusuu

print(ans)
