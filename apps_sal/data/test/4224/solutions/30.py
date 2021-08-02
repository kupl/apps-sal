n = int(input())
a_list = list(map(int, input().split()))

num_of_factor_2 = []

for i in range(len(a_list)):
    a_trial = 0
    while a_list[i] % 2 == 0:
        a_list[i] = a_list[i] / 2
        a_trial += 1
    num_of_factor_2.append(a_trial)

print(sum(num_of_factor_2))
