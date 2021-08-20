S_list = [input() for i in range(2)]
(N, K) = map(int, S_list[0].split())
h_list = list(map(int, S_list[1].split()))
number = 0
for i in h_list:
    if i >= K:
        number += 1
print(number)
