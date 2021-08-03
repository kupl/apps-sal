# 遇奇
# 同じカードが3枚以上あるときはそのカードだけを選び続けることで最終的に1枚か2枚にできる
# （最初に奇数枚あったら1 偶数枚なら2）
# そうして圧縮した山で、2枚あるものどうしはそれらを選ぶことで両方とも1枚にできる
# なので、圧縮した山に含まれる2枚の数の遇奇になる
n = int(input())
d = [0] * (10**5 + 1)
a = list(map(int, input().split()))
varies = len(set(a))
for v in a:
    d[v] += 1
two = 0
for i in range(len(d)):
    if d[i] > 0 and d[i] % 2 == 0:
        two += 1
print((varies if two % 2 == 0 else varies - 1))
