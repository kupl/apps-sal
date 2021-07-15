num = int(input())
cards = input().split(' ')

for i in range(num):
    cards[i] = int(cards[i])

num_5 = 0
num_0 = 0
result = ''
for i in range(num):
    if cards[i] == 5:
        num_5 += 1
    if cards[i] == 0:
        num_0 += 1

if num_0 == 0:
    print(-1)
elif num_5 // 9 < 0:
    print(-1)
else:
    result = '5' * ((num_5 // 9) * 9) + '0' * num_0
    print(int(result))

