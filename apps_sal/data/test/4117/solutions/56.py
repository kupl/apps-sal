n = int(input())
l_list = list(map(int, input().split()))

len_l = len(l_list)
l_list = sorted(l_list)
cnt = 0
for i in range(len_l - 2):
    for j in range(i + 1, len_l - 1):
        for k in range(j + 1, n):
            a = l_list[i]
            b = l_list[j]
            c = l_list[k]
            if a != b != c and a + b > c:
                cnt += 1
print(cnt)
