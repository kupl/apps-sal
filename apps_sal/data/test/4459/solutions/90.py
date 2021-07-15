from collections import Counter
N = int(input())
a = list(map(int, input().split()))
a_counter = Counter(a)

ans = 0

if N == 1 and a[0] != 1:
    print(1)
    return
elif N == 1 and a[0] == 1:
    print(0)
    return


for i in (a_counter.items()):
    key = (i[0])
    value = (i[1])

    if key == value:
        pass
    
    elif key < value:
        ans = ans + (value - key)
    else:
        ans = ans + (value) 

print(ans)
