n = int(input()) + 1
a = [0] + list(map(int, input().split()))
ans = 0
power = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        delta = a[i + 1]-a[i]
        dd = min(delta, power)
        delta -= dd
        power -= dd
        ans+=delta
    else:
        power+=a[i]-a[i+1]
print(ans)
