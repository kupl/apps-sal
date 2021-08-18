dishes = [int(input()) for i in range(5)]

d = [abs(d % 10 - 10) for d in dishes if d % 10 != 0]
if d:
    d.remove(max(d))
print(sum(dishes) + sum(d))
