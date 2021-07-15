n = int(input())
left = 1
right = n

def modulate(k):
    e = n
    Vasya = 0
    Petya = 0
    while e > 0:
        #print(e)
        if e <= k:
            Vasya += e
            break
        diff = e - k
        Vasya += k
        e -= k
        if e >= 10:
            Petya +=  diff // 10
            e -= diff // 10
        #print(e, ' left')
    #print(Vasya, 'ate Vasya overall')
    #print(Petya, 'ate Petya overall')
    if Vasya >= Petya:
        return True
    else:
        return False

while right - left > 1:
    middle = (right + left) // 2
    if not modulate(middle):
        left = middle
    else:
        right = middle

if modulate(left):
    print(left)
else:
    print(right)

