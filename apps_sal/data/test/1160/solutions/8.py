__author__ = 'Think'
assign = {'S': 0, 'M': 1, 'L': 2, 'XL': 3, 'XXL': 4, 'XXXL': 5, 'S,M': 6, 'M,L': 7, 'L,XL': 8, 'XL,XXL': 9, 'XXL,XXXL': 10}
up = {'S,M': 'M', 'M,L': 'L', 'L,XL': 'XL', 'XL,XXL': 'XXL', 'XXL,XXXL': 'XXXL'}
down = {'S,M': 'S', 'M,L': 'M', 'L,XL': 'L', 'XL,XXL': 'XL', 'XXL,XXXL': 'XXL'}
shirts = {i: 0 for i in range(11)}
numbers = [int(i) for i in input().split()]
split = {i: 0 for i in range(6, 11)}
n = int(input())
failed = False
received = []
for i in range(n):
    s = input()
    shirts[assign[s]] += 1
    received.append(s)
for i in range(6):
    numbers[i] -= shirts[i]
    if numbers[i] < 0:
        print('NO')
        failed = True
        break
if not failed:
    for i in range(6, 11):
        below = numbers[i - 6]
        above = numbers[i - 5]
        needed = shirts[i]
        if below >= needed:
            split[i] = needed
        else:
            split[i] = below
            needed -= below
            if above < needed:
                failed = True
                print('NO')
                break
            else:
                numbers[i - 5] -= needed
    if not failed:
        print('YES')
        for s in received:
            if assign[s] < 6:
                print(s)
            elif split[assign[s]] > 0:
                split[assign[s]] -= 1
                print(down[s])
            else:
                print(up[s])
