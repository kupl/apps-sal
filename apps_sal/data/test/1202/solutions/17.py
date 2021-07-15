# n = 4
# semi1 = [0, 9900, 9940, 10000, 10060]
# semi2 = [0, 9850, 9930, 10020, 10110]
n = int(input())
semi1 = [0] * (n + 1)
semi2 = [0] * (n + 1)

for i in range(1, n + 1):
    semi1[i], semi2[i] = map(int, input().split())

semi1Selected = [0] * (n + 1)
semi2Selected = [0] * (n + 1)


for i in range(1, n + 1):
    if i <= n // 2:
        semi1Selected[i] = 1
        semi2Selected[i] = 1
    else:
        if semi1[i] < semi2[n - i + 1]:
            semi1Selected[i] = 1

        if semi2[i] < semi1[n - i + 1]:
            semi2Selected[i] = 1


for i in range(1, n + 1):
    print(semi1Selected[i], end="")
print()
for i in range(1, n + 1):
    print(semi2Selected[i], end="")

