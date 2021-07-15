n = int(input())
a_list = sorted([int(x) for x in input().split()], reverse=True)
m = n
if m % 2 == 1:
    a_list.append(0)
    m += 1
for i in range(0, m, 2):
    if not (a_list[i] == a_list[i + 1] == n - (i + 1)):
        print(0)
        return
print(2 ** (n // 2) % (10 ** 9 + 7))
