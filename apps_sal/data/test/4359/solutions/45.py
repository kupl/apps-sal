duration = [0] * 5
duration[0] = int(input())
duration[1] = int(input())
duration[2] = int(input())
duration[3] = int(input())
duration[4] = int(input())

digit = list(map(lambda x: x % 10, duration))
if any(x != 0 for x in digit):
    least = min([x for x in digit if x != 0])
    idx = digit.index(least)
else:
    idx = 0

ans = 0
for i in range(5):
    if i != idx:
        ans += ((duration[i] + 9) // 10) * 10
    else:
        ans += duration[i]

print(ans)
