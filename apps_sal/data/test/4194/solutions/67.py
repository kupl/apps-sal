list = []
n, m = map(int, input().split())
a = input().split()[0:m]
for num in a:
    num = int(num)
    list.append(num)

answer = n - sum(list)
if n < sum(list):
    answer = -1

print(answer)
