nice = [1]
while nice[-1] <= 10**18:
    nice.append((nice[-1]<<1)+1)
for i in range(len(nice)):
    nice[i] = nice[i] * (nice[i] + 1) // 2

t = int(input())
for _ in range(t):
    x = int(input())
    i = 0
    num = 0
    while x > 0 and i < len(nice):
        if x >= nice[i]:
            x -= nice[i]
            num += 1
        i += 1
    print(num)
