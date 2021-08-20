(n, l) = map(int, input().split())
apple = [l + i for i in range(n)]
s = 0
while True:
    if s in apple:
        apple.remove(s)
        break
    elif abs(s) in apple:
        apple.remove(abs(s))
        break
    s -= 1
print(sum(apple))
