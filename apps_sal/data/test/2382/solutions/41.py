n = int(input())
a = [int(i) for i in input().split()]
a.sort()

big =  [a[-1]]
rest = a[:-1]


for i in range(n):
    not_yet = []
    count = 0
    for b in big:
        if count==2**i:
            break
        while rest:
            r = rest.pop()
            if r < b:
                big.append(r)
                count += 1
                break
            not_yet.append(r)
    big.sort(reverse=True)
    rest += not_yet[::-1]
print("Yes" if len(rest)==0 else "No")
