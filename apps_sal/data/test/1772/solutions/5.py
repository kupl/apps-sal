n = int(input())
mas = map(int, input().split())

odd = 0
even = 0
for i in mas:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

ans = min(odd, even)
odd = odd - ans
ans += int(odd / 3)
print(ans)
