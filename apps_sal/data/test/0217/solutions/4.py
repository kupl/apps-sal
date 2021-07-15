a, b, f, k = list(map(int, input().split()))
refill = b
busPos = 0
counter =0 

shouldPrint = True
while True:
    # Move to f
    busPos += f
    b -= f

    if b < 0:
        print(-1)
        shouldPrint = False
        break
    
    if (2 if k > 1 else 1) * (a - f) > b:
        b = refill
        counter += 1

    # Move to a
    busPos += (a - f)
    b -= (a - f)

    if b < 0:
        print(-1)
        shouldPrint = False
        break
    
    k -= 1
    if k == 0:
        break

    # Move back to f
    busPos -= (a - f)
    b -= (a - f)

    if b < 0:
        print(-1)
        shouldPrint = False
        break
    
    if (2 if k > 1 else 1) * f > b:
        b = refill
        counter += 1

    # Move back to start
    busPos -= f
    b -= f

    if b < 0:
        print(-1)
        shouldPrint = False
        break
    
    k -= 1
    if k == 0:
        break

if shouldPrint:
    print(counter)


