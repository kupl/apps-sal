n = int(input())

a_list = [int(i) for i in input().split()]
b_list = [int(i) for i in input().split()]
c_list = [int(i) for i in input().split()]

satisfaction = 0

for i in range(n):
    satisfaction += b_list[a_list[i] - 1]
    if i < n - 1:

        if a_list[i + 1] == a_list[i] + 1:
            satisfaction += c_list[a_list[i] - 1]

print(satisfaction)
