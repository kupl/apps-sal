t = int(input())
for i in range(t):
    n = int(input())
    a = set(map(int, input().split()))
    # print(a)
    even_numbers = {x for x in a if x % 2 == 0}
    used_numbers = set()
    k = 0
    for x in even_numbers:
        while x % 2 == 0 and x not in used_numbers:
            used_numbers.add(x)
            x //= 2
            k += 1
    print(k)
