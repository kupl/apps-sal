S_list = [input() for i in range(2)]
N = map(int, S_list[0].split())
A_list = list(map(int, S_list[1].split()))
print(max(A_list) - min(A_list))
