def base3(n):
    # 17 -> [2, 2, 1] (reversedd)
    array = []
    while n > 0:
        array.append(n % 3)
        n //= 3
    return array
def good(n):
    return 2 not in base3(n)

for _ in range(int(input())):
    n = int(input())
    while not good(n): n += 1
    print(n)
