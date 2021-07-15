import sys 

K = int(input())

if K <= 0:
    return

step = 1 
snuke = 1 

while K > 0:
    if step < snuke/sum(map(int, str(snuke))):
        snuke += 9 * step
        step *= 10
    else:
        print(snuke)
        snuke += step
        K -= 1
