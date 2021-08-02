def badges(b, g, n):
    p = [(i, n - i) for i in range(n + 1)]
    count = 0
    for i in p:
        if i[0] <= b and i[1] <= g:
            count += 1
    return count


b = int(input())
g = int(input())
n = int(input())
print(badges(b, g, n))
