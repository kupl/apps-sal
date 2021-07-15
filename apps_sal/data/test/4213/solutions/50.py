S_list = [input() for i in range(2)]
N = map(int,S_list[0].split())    
A_list = list(map(int,S_list[1].split()))

A_max = max(A_list)
A_min = min(A_list)
A_abs = abs(A_max - A_min)
print(A_abs)
