(A, B, C) = map(int, input().split(' '))
mod = []
pivot = 1
step = 1
while True:
    pivot = step * A % B
    if step * A % B == C:
        print('YES')
        break
    elif pivot in mod:
        print('NO')
        break
    else:
        mod.append(pivot)
        step = step + 1
