t = int(input())
for i in range(t):
    (l, v, l2, r) = list(map(int, input().split()))
    l2 -= 1
    num = l2 // v
    num2 = r // v
    print(l // v + num - num2)
