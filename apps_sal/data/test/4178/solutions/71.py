N = int(input())
H = list(map(int, input().split()))

a = 0
for i in H:
    if a <= i:
        a = i
    elif a - i >= 2:
        print('No')
        return
print('Yes')
