n = int(input())
a = int(input())
b = int(input())
c = int(input())

house = 'rab'
answer = 0

for i in range(n - 1):
    if house == 'rab':
        if a < b:
            house = 'owl'
            answer += a
        else:
            house = 'eey'
            answer += b
    elif house == 'owl':
        if a < c:
            house = 'rab'
            answer += a
        else:
            house = 'eey'
            answer += c
    else:
        if b < c:
            house = 'rab'
            answer += b
        else:
            house = 'owl'
            answer += c

print(answer)

