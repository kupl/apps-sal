n = int(input())
s_list = []
for i in range(n):
    (s, p) = input().split()
    p = int(p) * -1
    s_list.append([s, p, i + 1])
s_list.sort()
for i in s_list:
    print(i[2])
