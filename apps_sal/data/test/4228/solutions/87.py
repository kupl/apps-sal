lst = list(map(int, input().split()))
N = lst[0]
L = lst[1]
apple_flavours = []
for i in range(1, N + 1):
    apple_flavours.append(L + i - 1)
abs_apple_flavours = []
for apple in apple_flavours:
    abs_apple_flavours.append(abs(apple))
min_val = min(abs_apple_flavours)
index = abs_apple_flavours.index(min_val)
total_flavour = 0
for apple in apple_flavours:
    total_flavour += apple
print(total_flavour - apple_flavours[index])
