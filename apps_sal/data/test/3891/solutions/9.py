n, m = list(map(int, input().split()))
x = 0
y = 0
k = 0
for i in range(1, n + 1):
    s = input()
    if 'B' in s:
        if k == 0:
            x = i
            y = s.find('B') + 1
        k += 1
print(x + k // 2, y + k // 2)


        

