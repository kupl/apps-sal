n = int(input())
cards = list(map(int, input().split()))
five = cards.count(5) - (cards.count(5) % 9)
zero = cards.count(0)
if zero == 0:
    print(-1)
elif five == 0:
    print(0)
else:
    print('5' * five + zero * '0')
