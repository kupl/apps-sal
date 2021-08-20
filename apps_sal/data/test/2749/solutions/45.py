(H, W) = map(int, input().split())
N = int(input())
a = list(map(int, input().split()))
l_list = []
for i in range(N):
    l_list += [i + 1] * a[i]
judge = 0
for i in range(H):
    p_list = l_list[i * W:(i + 1) * W]
    if judge % 2 == 1:
        p_list = p_list[::-1]
    for j in p_list:
        print(j, end=' ')
    print()
    judge += 1
