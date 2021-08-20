n = int(input())
problems = [int(input()) for _ in range(n)]
sum_all = sum(problems)
not_multi_of_10 = [x for x in problems if x % 10 != 0]
not_multi_of_10.sort()
if sum_all % 10:
    print(sum_all)
elif len(not_multi_of_10) == 0:
    print(0)
else:
    print(sum_all - not_multi_of_10[0])
