n = int(input())
a = list(map(int, input().split()))
# count = 0
# list a[i]が偶数かどうかをチェック。ループはとりあえず省略する

exist_odd = False
# in_if = 0
in_for = 0
# in_while = 0
while exist_odd == False:
    for i in range(n):
        if a[i] % 2 != 0:
            exist_odd = True
            if n != i:
                in_for -= 1
            break
        else:
            a[i] = a[i] / 2
        # in_if += 1
        # print(in_if)
    in_for += 1
print(in_for)
