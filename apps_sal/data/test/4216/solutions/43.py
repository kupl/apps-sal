n = int(input())

def divs(n:int) -> list:
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n//i)
    divs.sort()
    return divs

div_l = divs(n)
print((max(len(str(div_l[(len(div_l)//2)-1])), len(str(div_l[len(div_l)//2])))))

