x, n = list(map(int, input().split()))
p = list(map(int, input().split()))

for i in range(100):
    num = x - i
    if num not in p:
        print(num)
        return
    num = x + i
    if num not in p:
        print(num)
        return
