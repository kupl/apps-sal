n = int(input())
inf = 2**32 - 1
x = 0
mult = [1]
uk = 0
amount = 1
for i in range(n):
    l = list(input().split())
    if l[0] == "for":
        mult.append(int(l[1]))
    if l[0] == "end":
        if (uk + 1 == len(mult)):
            amount //= mult[-1]
        mult.pop()
        if (uk == len(mult)):
            uk -= 1
    if l[0] == "add":
        while uk < len(mult) - 1:
            uk += 1
            amount *= mult[uk]
            if amount > inf:
                print('OVERFLOW!!!')
                return
        x += amount
        if (x > inf):
            print('OVERFLOW!!!')
            return
print(x)
