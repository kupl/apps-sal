


h, n = list(map(int, input().split()))
h += 1

moves = []

result = h - 1

n += (2**(h-1)) - 1

while n != 1:
    if n % 2 == 1:
        moves.append(1)
    else:
        moves.append(0)
    n //= 2

index_on_list = 0

ch = 1

while len(moves) > 0:
    if moves[-1] != index_on_list % 2:
        result += (2**(h-ch)) - 1
    else:
        moves.pop()
        ch += 1

    index_on_list += 1

print(result)




