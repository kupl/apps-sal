def govno():
    for i in range(len(num) - 1):
        if abs(num[i] - num[i + 1]) >= 2:
            if num[i] < num[i + 1]:
                num[i + 1] -= 1
                num[i] += 1
            else:
                num[i] -= 1
                num[i + 1] += 1


n = int(input())
num = list(map(int, input().split()))
cor = []
cor += num
cor.sort()
our = []
for i in range(n):
    govno()
    a = max(num)
    num.pop(num.index(a))
    our.append(a)
our.reverse()
if our == cor:
    print('YES')
else:
    print('NO')
